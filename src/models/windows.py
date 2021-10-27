from src.app import db


class Windows(db.Model):
    __tablename__ = 'windows'
    id = db.Column(
        db.Integer(),
        primary_key=True,
    )
    x = db.Column(
        db.Integer(),
        nullable=False,
    )
    y = db.Column(
        db.Integer(),
        nullable=False,
    )
