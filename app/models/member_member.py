from app import db

class MemberMember(db.Model):
    __tablename__ = "member_member"
    parent_id = db.Column(db.Integer, db.ForeignKey("member.id"), primary_key=True,nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey("member.id"), primary_key=True,nullable=False)