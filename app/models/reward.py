from app import db

class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    title = db.Column(db.String)
    points = db.Column(db.Integer)
    users = db.relationship("User",  back_populates="reward")

