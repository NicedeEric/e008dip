from src.app import db


class Tables(db.Model):
    __tablename__ = 'tables'
    id = db.Column(
        db.Integer(),
        primary_key=True,
    )
    topLeft = db.Column(
        db.String(64),
        nullable=False,
    )
    topRight = db.Column(
        db.String(64),
        nullable=False,
    )
    bottomLeft = db.Column(
        db.String(64),
        nullable=False,
    )
    bottomRight = db.Column(
        db.String(64),
        nullable=False,
    )
