#ok
from app import db
from sqlalchemy import Column, Integer, Date, String


class KlogPosts(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)

    title = Column(String(150), nullable=False)
    date = Column(Date, nullable=False)
    contents = Column(String, nullable=False)
    author = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)