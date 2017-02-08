# -*- coding: utf-8 -*-
import datetime
import enum
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, ForeignKey
from sqlalchemy import Float

from app import db
from app.models.user_model import UserModel


class CapsuleModel(db.Model):
    __tablename__ = 'capsules'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    school_id = Column(Integer, ForeignKey('schools.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    private = Column(Boolean, nullable=False, default=False)
    locked = Column(Boolean, nullable=False, default=True)
    # minimum_at = Column(DateTime, nullable=False)
    # maximum_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    latitude = Column(Float, nullable=False, default=-1)
    longitude = Column(Float, nullable=False, default=-1)
    content = Column(String(255), default='')
    title = Column(String(255), default='')

    def __init__(self, user_id=None, school_id=None, locked=None, minimum_at=None, maximum_at=None, latitude=None,
                 longitude=None, content=None, title=None):
        self.user_id = user_id
        self.school_id = school_id
        self.locked = locked
        #  self.minimum_at = minimum_at
        #  self.maximum_at = maximum_at
        self.latitude = latitude
        self.longitude = longitude
        self.content = content
        self.title = title


def get_capsules():
    return CapsuleModel.query


def get_capsules_by_id(capsule_id):
    return CapsuleModel.query.filter(CapsuleModel.id == capsule_id).first()


def is_capsule_open(capsule_id):
    capsule = CapsuleModel.query.filter(CapsuleModel.id == capsule_id).first()

    if capsule.locked:
        return False
    else:
        return True
