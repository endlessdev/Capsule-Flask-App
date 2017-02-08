# -*- coding: utf-8 -*-


def serialize_activity(activity):
    return {
        'id': activity.id,
        'user_id': activity.user_id,
        'content': activity.content,
        'created_at': str(activity.created_at)
    }
