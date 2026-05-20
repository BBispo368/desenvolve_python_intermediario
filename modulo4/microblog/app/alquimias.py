from app import db
from app.models.models import User, Post
from sqlalchemy import select, desc
from datetime import datetime

def validate_user_password(username, password):
    stmt = select(User).filter_by(username=username)
    user = db.session.execute(stmt).scalars().first()
    if user and user.password == password:
        return user
    return None

def user_exists(username):
    stmt = select(User).filter_by(username=username)
    return db.session.execute(stmt).scalars().first()

def create_user(username, password, foto=None, bio=None, remember=False, last_login=None):
    new_user = User(
        username=username,
        password=password,
        foto=foto,
        bio=bio,
        last_login=last_login or datetime.utcnow()
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def create_post(body, author):
    new_post = Post(
        body=body,
        author=author,
        timestamp=datetime.utcnow()
    )
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_timeline():
    stmt = select(Post).order_by(desc(Post.timestamp)).limit(5)
    return db.session.execute(stmt).scalars().all()
