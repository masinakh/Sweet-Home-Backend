from app import db

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True,autoincrement = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    is_parent = db.Column(db.Boolean, default=False)
    chores = db.relationship("Chore", back_populates = "user")
    rewards = db.relationship("Reward", secondary="user_reward", backref="users")
    users = db.relationship("User", secondary="user_user", backref="users")

