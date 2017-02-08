# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app import basic_auth
from app.models.user_token_model import token_generate
from app.modules import capsule
from app.models.user_model import users_auth

_URL = '/auth'


class Auth(Resource):
    @capsule.API
    def post(self):
        email = request.form.get('email', None)
        password = request.form.get('password', None)

        print('auth email : ', email)
        print('password email : ', password)
        if users_auth(email, password):
            _return = {
                'data': token_generate(email=email)
            }

            return _return, status.HTTP_200_OK
        else:
            return "auth failed ", status.HTTP_401_UNAUTHORIZED
