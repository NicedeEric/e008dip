from src.app import db


class Walls(db.Model):
    __tablename__ = 'walls'
    id = db.Column(
        db.Integer(),
        primary_key=True,
    )
    point1 = db.Column(
        db.String(64),
        nullable=False,
    )
    point2 = db.Column(
        db.String(64),
        nullable=False,
    )
    point3 = db.Column(
        db.String(64),
        nullable=False,
    )
    point4 = db.Column(
        db.String(64),
        nullable=False,
    )
    point5 = db.Column(
        db.String(64),
        nullable=False,
    )
    point6 = db.Column(
        db.String(64),
        nullable=False,
    )
