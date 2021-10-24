from src.app import db


class Nodes(db.Model):
    __tablename__ = 'nodes'
    id = db.Column(
        db.Integer(),
        primary_key=True,
    )
    name = db.Column(
        db.String(64),
        nullable=False,
        unique=True,
    )
    x = db.Column(
        db.Integer(),
        nullable=False,
    )
    y = db.Column(
        db.Integer(),
        nullable=False,
    )
