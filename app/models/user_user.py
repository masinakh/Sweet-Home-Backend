from app import db

class UserUser(db.Model):
    __tablename__ = "user_user"
    parent_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True,nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True,nullable=False)