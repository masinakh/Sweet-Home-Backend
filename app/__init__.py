from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS

import os
db = SQLAlchemy()
migrate = Migrate()
load_dotenv()
def create_app(test_config=None):
    app = Flask(__name__)
    # app.config["SESSION_COOKIE_DOMAIN"] = "127.0.0.1:5000 127.0.0.1:3000"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")
    # Import models here for Alembic setup
   
    from app.models.chore import Chore
    from app.models.reward import Reward
    from app.models.member import Member
    from app.models.member_reward import MemberReward
    from app.models.family import Family
    db.init_app(app)
    migrate.init_app(app, db)
    # Register Blueprints here
    from .routes.chore import chore_bp
    app.register_blueprint(chore_bp)
    from .routes.reward import reward_bp
    app.register_blueprint(reward_bp)
    from .routes.member import member_bp
    app.register_blueprint(member_bp)
    from .routes.family import family_bp
    app.register_blueprint(family_bp)
    
    app.run(debug=True)
    CORS(app)
    return app
