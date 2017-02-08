# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Text, Integer

from app import db
from app.models.user_model import UserModel
from app.models.timeline_model import TimelineModel


class TimelineCommentModel(db.Model):
    __tablename__ = 'timeline_comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    post_id = Column(Integer, ForeignKey('timelines.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False, default='')
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, user_id=None, post_id=None, content=None):
        self.user_id = user_id
        self.post_id = post_id
        self.content = content


def get_post_comments(post_id=0):
    comments = []

    comments_query = TimelineCommentModel.query \
        .filter(TimelineCommentModel.post_id == post_id)

    for comment in comments_query:
        comments.append(comment)

    return comments
