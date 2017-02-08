# -*- coding: utf-8 -*-
from flask import json
from flask import request
from flask_api import status
from flask_restful import Resource

from app import token_auth, db
from app.models.capsule_model import is_capsule_open, get_capsules_by_id
from app.modules.capsule.serialize.capsule import serialize_capsule
from app.modules import capsule

_URL = '/capsules/<prefix>'


class CapsulesInfo(Resource):
    @capsule.API
    @token_auth.login_required
    def get(self, prefix):
        capsule_id = prefix

        if is_capsule_open(capsule_id):
            capsule = get_capsules_by_id(capsule_id)

            return serialize_capsule(capsule), status.HTTP_200_OK
        else:
            return "Capsule locked", status.HTTP_400_BAD_REQUEST
