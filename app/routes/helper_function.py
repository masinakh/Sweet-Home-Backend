from flask import abort, make_response, request, session
from app.models.member import Member


def get_model_from_id(cls,model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        return abort(make_response({"msg":f"Invalid id for model of type {cls.__name__}: {model_id}"}, 400 ))
    chosen_object = cls.query.get(model_id)
    if not chosen_object:
        return abort(make_response({"msg": f" Could not find item with id : {model_id}"} , 404 ))
    return chosen_object

def get_member_from_session():
    return Member(**session["member"])