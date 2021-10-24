from src.app import db


class Edges(db.Model):
    __tablename__ = 'edges'
    id = db.Column(
        db.Integer(),
        primary_key=True,
    )
    startPoint = db.Column(
        db.String(64),
        nullable=False,
    )
    endPoint = db.Column(
        db.String(64),
        nullable=False,
    )
    length = db.Column(
        db.Integer(),
        nullable=False,
    )
