from db import db


class TiktokLinkModel(db.Model):
    __tablename__ = "tiktokLinks"

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(80), unique=True, nullable=False)
    title = db.Column(db.String(200), unique=True, nullable=False)
    status = db.Column(db.Integer, unique=False, nullable=False, default=0)
