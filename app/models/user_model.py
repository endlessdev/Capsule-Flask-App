# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import Column, Integer, String, DateTime
from werkzeug.security import check_password_hash

from app import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    permission = Column(String(255), nullable=False, default='USER')
    updated_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, name=None, email=None, password=None, permission=None, updated_at=None):
        self.name = name
        self.email = email
        self.password = password
        self.permission = permission
        self.updated_at = updated_at


def get_user(user_id=0):
    user_query = UserModel.query \
        .filter(UserModel.id == user_id).first()

    return user_query


def get_user_with_email(email=None):
    user_query = UserModel.query \
        .filter(UserModel.email == email).first()

    return user_query


def get_user_with_id(user_id=None):
    user_query = UserModel.query.filter(UserModel.id == user_id).first()

    return user_query


def get_users():
    users = []

    users_query = UserModel.query.all()

    for user in users_query:
        users.append(user)

    return users


def users_auth(email=None, password=None):
    user = UserModel.query.filter(UserModel.email == email).first()

    return check_password_hash(user.password, password)
