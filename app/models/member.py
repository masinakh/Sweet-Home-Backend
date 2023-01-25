from app import db

class Member(db.Model):
    id= db.Column(db.Integer, primary_key=True,autoincrement = True, nullable= False)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    is_parent = db.Column(db.Boolean, default=False)
    chores = db.relationship("Chore", back_populates = "member")
    rewards = db.relationship("Reward", secondary="member_reward", backref="members")
    members = db.relationship("Member", secondary="member_member", backref="members")

