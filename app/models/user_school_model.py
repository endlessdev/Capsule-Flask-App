# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey

from app import db
from app.models.user_model import UserModel
from app.models.school_model import SchoolModel


class UserSchoolModel(db.Model):
    __tablename__ = 'user_schools'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    school_id = Column(Integer, ForeignKey('schools.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    admission_year = Column(Integer, nullable=False)
    graduation_year = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, user_id=None, school_id=None, admission_year=None, graduation_year=None):
        self.user_id = user_id
        self.school_id = school_id
        self.admission_year = admission_year
        self.graduation_year = graduation_year


def get_user_school(user_id=0):
    user_schools = []

    user_schools_query = UserSchoolModel.query \
        .filter(UserSchoolModel.user_id == user_id)

    for user_school in user_schools_query:
        user_schools.append(user_school)

    return user_schools