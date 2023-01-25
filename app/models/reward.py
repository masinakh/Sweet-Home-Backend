from app import db

class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement = True, nullable= False)
    title = db.Column(db.String)
    points = db.Column(db.Integer)
    members = db.relationship("Member", back_populates="rewards")

