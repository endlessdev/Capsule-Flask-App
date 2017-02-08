# -*- coding: utf-8 -*-
import json
import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text

from app import db


class RoleModel(db.Model):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    allow = Column(Text, nullable=False)
    updated_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, name=None, allow=None, updated_at=None):
        self.name = name
        self.allow = json.dumps(allow)
        self.updated_at = updated_at
