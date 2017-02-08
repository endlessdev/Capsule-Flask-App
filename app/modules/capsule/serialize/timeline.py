# -*- coding: utf-8 -*-
import requests

from app.config import GOOGLE_API_KEY
from app.models.user_model import get_user_with_id
from app.models.timeline_comment_model import get_post_comments
from app.modules.capsule.serialize.user import serialize_user


def _get_address(lat, lng):
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=%s' % (
        lat, lng, GOOGLE_API_KEY
    ))

    try:
        return r.json()['results'][0]['formatted_address']
    except (ValueError, KeyError, IndexError):
        return None


def serialize_post(post):
    return {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'latitude': post.latitude,
        'longitude': post.longitude,
        'address': _get_address(post.latitude, post.longitude),
        'comments': list(map(lambda comment: serialize_comment(comment), get_post_comments(post.id))),
        'created_at': post.created_at.isoformat()
    }


def serialize_comment(comment):
    return {
        'id': comment.id,
        'writer': serialize_user(get_user_with_id(comment.user_id)),
        'post_id': comment.post_id,
        'content': comment.content,
        'created_at': comment.created_at.isoformat()
    }
