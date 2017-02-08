# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey

from app import db
from app.models.user_model import UserModel
from app.models.role_model import RoleModel


class UserRoleModel(db.Model):
    __tablename__ = 'user_roles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    comment = Column(String(500))
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, user_id=None, role_id=None, comment=None):
        self.user_id = user_id
        self.role_id = role_id
        self.comment = comment
