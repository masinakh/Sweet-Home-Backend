from app import db

class Chore(db.Model):
    id= db.Column(db.Integer, primary_key=True,autoincrement = True , nullable= False)
    title = db.Column(db.String)
    points = db.Column(db.Integer)
    is_completed = db.Column(db.Boolean, default=False)
    member_id = db.Column(db.Integer, db.ForeignKey("member.id" ), nullable = True)
    member = db.relationship("Member", back_populates = "chores")










