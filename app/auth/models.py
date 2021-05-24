from app import db

class User:
    __tablename__ = "users"
    firstName = db.Column(db.String(128))