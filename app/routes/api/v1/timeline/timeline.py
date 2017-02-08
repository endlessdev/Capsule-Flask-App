# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app import token_auth
from app.models.timeline_model import get_post
from app.modules import capsule
from app.modules.capsule.serialize.timeline import serialize_post

_URL = '/timeline/<prefix>'


class Timeline(Resource):
    @capsule.API
    @token_auth.login_required
    def get(self, prefix):
        try:
            post_id = int(prefix)

            post = get_post(post_id)

            if post is not None:
                return serialize_post(post), status.HTTP_200_OK

            return "It does not exist.", status.HTTP_404_NOT_FOUND
        except ValueError:
            return "Prefix can only be number.", status.HTTP_400_BAD_REQUEST
