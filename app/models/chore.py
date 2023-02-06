from app import db

class Chore(db.Model):
    id= db.Column(db.Integer, primary_key=True,autoincrement = True , nullable= False)
    title = db.Column(db.String)
    points = db.Column(db.Integer)
    is_completed = db.Column(db.Boolean, default=False)
    member_id = db.Column(db.Integer, db.ForeignKey("member.id" ), nullable = True)
    member = db.relationship("Member", back_populates = "chores")
    family_id = db.Column(db.Integer, db.ForeignKey("family.id" ),  default=None)
    family = db.relationship("Family",back_populates = "chores" )

    def to_dict(self):
        return {
            "id":self.id,
            "title": self.title,
            "points": self.points,
            "is_completed": self.is_completed,
            "member_id": self.member_id,
            "family_id": self.family_id,
        }
    @classmethod
    def from_dict(cls, chore_dict):
        return Chore (
            title=chore_dict["title"],
            points=chore_dict["points"],
            family_id = chore_dict["familyId"]
        )









