# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app import token_auth
from app.models.school_model import get_schools
from app.modules import capsule
from app.modules.capsule.serialize.school import serialize_school

_URL = '/schools'


class Schools(Resource):
    @capsule.API
    def get(self):
        name = request.args.get('name', '')

        _return = {
            'data': []
        }

        schools = get_schools(name)

        for school in schools:
            _return['data'].append(serialize_school(school))

        return _return, status.HTTP_200_OK
