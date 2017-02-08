# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime

from app import db


class SchoolModel(db.Model):
    __tablename__ = 'schools'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    address = Column(String(500), nullable=False)
    link = Column(String(255), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __init__(self, name=None, address=None, link=None, latitude=None, longitude=None):
        self.name = name
        self.address = address
        self.link = link
        self.latitude = latitude
        self.longitude = longitude


def get_school(school_id=0):
    school_query = SchoolModel.query \
        .filter(SchoolModel.id == school_id).first()

    return school_query


def get_schools(name=None):
    schools = []

    if name == 'all':
        schools_query = SchoolModel.query \
            .all()
    else:
        schools_query = SchoolModel.query \
            .filter(SchoolModel.name.like('' if name is None else str(name) + '%')) \
            .order_by(SchoolModel.id.desc()) \
            .limit(10)

    for school in schools_query:
        schools.append(school)

    return schools
