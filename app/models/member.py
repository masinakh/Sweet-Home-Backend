from app import db

class Member(db.Model):
    id= db.Column(db.Integer, primary_key=True,autoincrement = True, nullable= False)
    name = db.Column(db.String)
    email = db.Column(db.String)
    # password = db.Column(db.String)
    points = db.Column(db.Integer, default=0)
    is_parent = db.Column(db.Boolean, default=False)
    chores = db.relationship("Chore", back_populates = "member")
    rewards = db.relationship("Reward", secondary="member_reward", back_populates="members")
    family_id = db.Column(db.Integer, db.ForeignKey("family.id" ), nullable = True)
    family = db.relationship("Family",back_populates = "members" )

    def to_dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "email": self.email,
            "points": self.points,
            "is_parent": self.is_parent,
            "family_id": self.family_id,
        }

    @classmethod
    def from_dict(cls, member_dict):
        return Member (
            name=member_dict["name"],
            email = member_dict["email"],
            is_parent = member_dict["isParent"],
            family_id = member_dict["familyId"]
        )



