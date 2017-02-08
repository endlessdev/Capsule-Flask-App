# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app import db
from app.models.user_model import UserModel


class UserActivitiesModel(db.Model):
    __tablename__ = 'user_activities'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    content = Column(String(255), nullable=False, default='')
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, user_id=None, content=None):
        self.user_id = user_id
        self.content = content


def get_activities_by_id(user_id):
    activities_query = UserActivitiesModel.query \
        .filter(UserActivitiesModel.user_id == user_id)

    return activities_query
