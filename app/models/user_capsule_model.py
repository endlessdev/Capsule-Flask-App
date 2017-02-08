# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, ForeignKey

from app import db
from app.models.user_model import UserModel
from app.models.capsule_model import CapsuleModel


class UserCapsuleModel(db.Model):
    __tablename__ = 'user_capsule'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    capsule_id = Column(Integer, ForeignKey('capsules.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, user_id=None, capsule_id=None):
        self.user_id = user_id
        self.capsule_id = capsule_id


def get_users_num_by_capsule_id(capsule_id):
    return UserCapsuleModel.query.filter(UserCapsuleModel.id == capsule_id).first()
