# -*- coding: utf-8 -*-
from flask_api import status
from flask_restful import Resource

from app.config import ENVIRONMENT, API_VERSION, APP_VERSION
from app.modules import capsule


_URL = '/'


class Index(Resource):
    @capsule.API
    def get(self):
        _return = {
            'environment': ENVIRONMENT,
            'version': {
                'api': API_VERSION,
                'app': APP_VERSION
            }
        }

        return _return, status.HTTP_200_OK
