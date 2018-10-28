from exts import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(100),primary_key=True)
    username = db.Column(db.String(100),nullable=False)
    telephone = db.Column(db.String(11),nullable=False)
    password = db.Column(db.String(100),nullable=False)

