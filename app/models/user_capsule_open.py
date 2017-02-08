# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, ForeignKey

from app import db
from app.models.user_model import UserModel
from app.models.capsule_model import CapsuleModel


class UserCapsuleOpenModel(db.Model):
    __tablename__ = "user_capsule_open"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    capsule_id = Column(Integer, ForeignKey('capsules.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now);

    def __init__(self, user_id=None, capsule_id=None):
        self.user_id = user_id
        self.capsule_id = capsule_id


def get_requested_friends_num(capsule_id):
    result = 0
    requests = UserCapsuleOpenModel.query.filter(UserCapsuleOpenModel.capsule_id == capsule_id)

    for request in requests:
        current_time = datetime.datetime.now()
        request_time = requests.created_at

        if current_time - request_time < datetime.timedelta(minutes=10):
            result += 1

    return result
