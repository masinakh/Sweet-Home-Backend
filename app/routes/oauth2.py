import os
import pathlib
import requests
from app import db
from flask import Flask, session, abort, redirect, request,Blueprint
from functools import wraps
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from app.models.member import Member
from app.models.family import Family

oauth_bp = Blueprint("oauth_bp", __name__, url_prefix="/")

# app = Flask("Google Login App")


 # make sure this matches with that's in client_secret.json

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" # to allow Http traffic for local dev

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)


def login_is_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function(*args, **kwargs)

    return wrapper


@oauth_bp.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    # print(authorization_url)
    # print(request.args)
    session["create_family"] = request.args.get("create_family",False)
    return redirect(authorization_url)
# print("test")

@oauth_bp.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    # print(session["google_id"])
    member = Member.query.filter(Member.email== id_info.get("email")).first()
    
    if not member:
        member = Member(name= id_info.get("name"), email= id_info.get("email"))
        db.session.add(member)
        db.session.commit()
    if session["create_family"] and not member.family_id:
        family = Family()
        db.session.add(family)
        db.session.commit()
        member.family_id = family.id
        member.is_parent = True
        db.session.add(member)
        db.session.commit()
    # print(session)
    session['member'] = member.to_dict()
    # print(session['member'])
    
    return redirect("/protected_area")
    


@oauth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@oauth_bp.route("/")
def index():
    return "Hello World <a href='/login'><button class='login-with-google-btn'> Sign with Google</button></a>"


@oauth_bp.route("/protected_area")
@login_is_required
def protected_area():
    return f"Hello {session['name']}! </br> <a href='/logout'><button>Logout</button></a>"


# if __name__ == "__main__":
#     # app.run(host='0.0.0.0', port=80, debug=True)
#     