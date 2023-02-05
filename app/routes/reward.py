from flask import Blueprint, jsonify, request
from app import db
from app.models.member import Member
from app.models.member_reward import MemberReward
from app.models.reward import Reward
from sqlalchemy import or_
from .helper_function import get_model_from_id


reward_bp = Blueprint("reward_bp", __name__, url_prefix="/rewards")

@reward_bp.route("/<family_id>", methods=["GET"])
def get_all_rewards(family_id):
    rewards = Reward.query.filter(Reward.family_id == int(family_id)).all() 
    reward_list = [reward.to_dict() for reward in rewards]
    return jsonify(reward_list), 200


@reward_bp.route("", methods=["POST"])
def create_new_reward():
    request_body = request.get_json()
    try:
        new_reward = Reward.from_dict(request_body)
        db.session.add(new_reward)
        db.session.commit()
    except KeyError:
        return jsonify({"msg":"invalid_data"}), 400
    return jsonify(f"Reward {new_reward.title} successfully created"), 201


@reward_bp.route("/<reward_id>/<member_id>", methods=["PATCH"])
def select_one_reward(reward_id, member_id):
    reward= get_model_from_id(Reward, reward_id)
    member= get_model_from_id(Member, member_id)
    if member.points < reward.points:
        return jsonify({"msg": "you don't have enough points, do more chores"})
    member.points -= reward.points
    new_member_reward = MemberReward.create(member_id, reward_id)
    db.session.add(new_member_reward)
    db.session.commit()
    return jsonify({"reward":reward.to_dict()}),200


@reward_bp.route('/<reward_id>', methods= ['DELETE'])
def delete_one_reward(reward_id):
    reward_to_delete = get_model_from_id(Reward, reward_id)
    db.session.delete(reward_to_delete)
    db.session.commit()
    return jsonify({
            "details": f'Reward {reward_to_delete.id} "{reward_to_delete.title}" successfully deleted'
            }), 200