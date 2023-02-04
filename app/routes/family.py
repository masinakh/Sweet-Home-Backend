from flask import Blueprint, jsonify, request
from app import db
# from app.models.chore import Chore
# from app.models.member import Member
from app.models.family import Family

from sqlalchemy import and_
from .helper_function import get_model_from_id
# from app.routes.oauth2 import login_is_required


family_bp = Blueprint("family_bp", __name__, url_prefix="/family")


@family_bp.route("", methods=["POST"])
def create_new_family():
    # request_body = request.get_json()
  
    new_family= Family()
    db.session.add(new_family)
    db.session.commit()
  
    return jsonify({"id":new_family.id}), 201
