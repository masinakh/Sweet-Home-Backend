from app import db

class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement = True, nullable= False)
    title = db.Column(db.String)
    points = db.Column(db.Integer)
    members = db.relationship("Member",secondary="member_reward", back_populates="rewards")
    family = db.relationship("Family",back_populates = "rewards" )
    family_id = db.Column(db.Integer, db.ForeignKey("family.id" ), nullable = False)

    def to_dict(self):
            return {
                "id":self.id,
                "title": self.title,
                "points": self.points,
                "family_id": self.family_id,
            }
    @classmethod
    def from_dict(cls, reward_dict):
        return Reward (
                title=reward_dict["title"],
                points=reward_dict["points"]
            )
