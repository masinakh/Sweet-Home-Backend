from app import db

class Family(db.Model):
    id= db.Column(db.Integer, primary_key=True,autoincrement = True , nullable= False)
    members = db.relationship("Member", back_populates = "family")