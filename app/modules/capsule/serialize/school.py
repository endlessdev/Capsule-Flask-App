# -*- coding: utf-8 -*-
import datetime


def serialize_school(school):
    return {
        'id': school.id,
        'name': school.name,
        'address': school.address,
        'link': school.link,
        'latitude': school.latitude,
        'longitude': school.longitude,
        'created_at': school.created_at.isoformat()
    }
