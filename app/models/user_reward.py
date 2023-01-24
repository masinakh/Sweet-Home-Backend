from app import db

class UserReward(db.Model):
    __tablename__ = "user_reward"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True,nullable=False)
    reward_id = db.Column(db.Integer, db.ForeignKey("reward.id"), primary_key=True,nullable=False)