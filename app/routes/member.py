from flask import Blueprint, jsonify, request
from app import db
from sqlalchemy import or_
from .helper_function import get_model_from_id
from app.models.member import Member

member_bp = Blueprint("member_bp", __name__, url_prefix="/members")

@member_bp.route("/<family_id>", methods=["GET"])
def get_all_family_members(family_id):
    members = Member.query.filter(Member.family_id == int(family_id)).all() 
    member_list = [member.to_dict() for member in members]
    return jsonify(member_list), 200

@member_bp.route("/<member_id>", methods=["GET"])
def get_one_member(member_id):
    member = get_model_from_id(Member,member_id)
    return jsonify(member), 200
    

@member_bp.route("", methods=["POST"])
def create_new_member():
    request_body = request.get_json()
    try:
        new_member = Member.from_dict(request_body)
        db.session.add(new_member)
        db.session.commit()
    except KeyError:
        return jsonify({"msg":"invalid_data"}), 400
    return jsonify(f"Member {new_member.name} successfully created"), 201


@member_bp.route('/<member_id>', methods= ['DELETE'])
def delete_one_family_member(member_id):
    member_to_delete = get_model_from_id(Member, member_id)
    db.session.delete(member_to_delete)
    db.session.commit()
    return jsonify({
            "details": f'Member {member_to_delete.id} {member_to_delete.name} successfully deleted'
            }), 200

