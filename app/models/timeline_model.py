# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Text, Integer, String, Float

from app import db
from app.models.user_model import UserModel


class TimelineModel(db.Model):
    __tablename__ = 'timelines'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False, default='')
    content = Column(Text, nullable=False, default='')
    latitude = Column(Float, nullable=False, default=-1)
    longitude = Column(Float, nullable=False, default=-1)
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, user_id=None, title=None, content=None, latitude=None, longitude=None):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.latitude = latitude
        self.longitude = longitude


def get_timeline(order='desc', page=0, limit=10):
    posts = []

    posts_query = TimelineModel.query \
        .order_by(TimelineModel.id.asc() if order == 'asc' else TimelineModel.id.desc()) \
        .limit(limit) \
        .offset(page * limit)

    for post in posts_query:
        posts.append(post)

    return posts


def get_post(post_id=0):
    post_query = TimelineModel.query \
        .filter(TimelineModel.id == post_id).first()

    return post_query
