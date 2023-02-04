from flask import Blueprint, jsonify, request
from app import db
# from app.models.chore import Chore
# from app.models.member import Member
from app.models.family import Family

family_bp = Blueprint("family_bp", __name__, url_prefix="/family")


@family_bp.route("", methods=["POST"])
def create_new_family():
    new_family= Family()
    db.session.add(new_family)
    db.session.commit()
    return jsonify({"id":new_family.id}), 201
