from app import db

class MemberReward(db.Model):
    __tablename__ = "member_reward"
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"), primary_key=True,nullable=False)
    reward_id = db.Column(db.Integer, db.ForeignKey("reward.id"), primary_key=True,nullable=False)
    
    @classmethod
    def create(cls, member_id, reward_id):
        return MemberReward(
            member_id = member_id, reward_id = reward_id
        )