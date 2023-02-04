from flask import Blueprint, jsonify, request
from app import db
from app.models.chore import Chore
from app.models.member import Member
from sqlalchemy import and_
from .helper_function import get_model_from_id

chore_bp = Blueprint("chore_bp", __name__, url_prefix="/chores")

@chore_bp.route("/<family_id>", methods=["GET"])
def get_all_chores(family_id):
    chores = Chore.query.filter(and_(Chore.member_id == None,Chore.family_id ==family_id)).all()  
    chores_list = [chore.to_dict() for chore in chores]
    return jsonify(chores_list), 200


@chore_bp.route("", methods=["POST"])
def create_new_chore():
    request_body = request.get_json()
    try:
        new_chore = Chore.from_dict(request_body)
        db.session.add(new_chore)
        db.session.commit()
    except KeyError:
        return jsonify({"msg":"invalid_data"}), 400
    return jsonify(f"chore {new_chore.title} successfully created"), 201
    

@chore_bp.route("/<chore_id>/<member_id>", methods=["PATCH"])
def set_member_to_chore(chore_id, member_id):
    chore= get_model_from_id(Chore, chore_id)
    chore.member_id=member_id
    db.session.commit()
    return jsonify({"chore":chore.to_dict()}),200


@chore_bp.route("/<chore_id>/mark_complete", methods=["PATCH"])
def update_chore(chore_id):
    chore= get_model_from_id(Chore, chore_id)
    if chore.member_id == None:
        return jsonify({"msg":"chore was not assigned"})
    chore.is_completed = not chore.is_completed
    points = chore.points if chore.is_completed else -1 * chore.points
    member_assigned = get_model_from_id(Member, chore.member_id)
    member_assigned.points += points
    db.session.commit()
    return jsonify({"chore":chore.to_dict()}),200



@chore_bp.route('/<chore_id>', methods= ['DELETE'])
def delete_one_chore(chore_id):
    chore_to_delete = get_model_from_id(Chore, chore_id)
    db.session.delete(chore_to_delete)
    db.session.commit()
    return jsonify({
            "details": f'Chore {chore_to_delete.id} "{chore_to_delete.title}" successfully deleted'
            }), 200










