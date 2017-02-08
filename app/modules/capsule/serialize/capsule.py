# -*- coding: utf-8 -*-


def serialize_capsule(capsule):
    return {
        'id': capsule.id,
        'latitude': capsule.latitude,
        'longitude': capsule.longitude,
        'title': capsule.title,
        'content': capsule.content,
        'school_id': capsule.school_id
    }
