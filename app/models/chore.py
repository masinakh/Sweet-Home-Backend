from app import db

class Chore(db.Model):
    id= db.Column(db.Integer, primary_key=True,autoincrement = True)
    title = db.Column(db.String)
    points = db.Column(db.Integer)
    is_completed = db.Column(db.bool, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id" ),nullable = True)
    user = db.relationship("User", back_populates = "chores")










