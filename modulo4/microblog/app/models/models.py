from datetime import datetime
from flask_login import UserMixin
from app import db, login
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, DateTime, ForeignKey

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(128))
    last_login: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=True)
    foto: Mapped[str] = mapped_column(String(256), nullable=True)
    bio: Mapped[str] = mapped_column(String(256), nullable=True)
    
    posts: Mapped[list['Post']] = relationship(back_populates='author')

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    body: Mapped[str] = mapped_column(String(280))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    author: Mapped[User] = relationship(back_populates='posts')

    def __repr__(self):
        return f'<Post {self.body[:30]}>'

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
