# -*- coding: utf-8 -*-
from flask import json
from flask import request
from flask_api import status
from flask_restful import Resource

from app import token_auth, db
from app.models.user_activities import get_activities_by_id
from app.modules.capsule.serialize.activity import serialize_activity
from app.modules import capsule

_URL = '/users/<prefix>/activities'


class UserActivities(Resource):
    @capsule.API
    @token_auth.login_required
    def get(self, prefix):
        _return = {
            'data': []
        }

        activities = get_activities_by_id(prefix)

        for activity in activities:
            _return['data'].append(serialize_activity(activity))

        return _return, status.HTTP_200_OK
