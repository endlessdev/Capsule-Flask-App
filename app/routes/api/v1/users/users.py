# -*- coding: utf-8 -*-
import re

from flask import request
from flask_api import status
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from app import db, token_auth
from app.config import DEFAULT_URL
from app.models.user_model import UserModel, get_users
from app.models.user_token_model import token_is_auth
from app.modules import capsule
from app.modules.capsule.validate import users as usersValidate
from app.modules.capsule.serialize.user import serialize_user

_URL = '/users'


class Users(Resource):
    @capsule.API
    def get(self):
        _return = {
            'data': []
        }

        users = get_users()

        for user in users:
            _return['data'].append(serialize_user(user))

        return _return, status.HTTP_200_OK

    @capsule.API
    def post(self):
        email = request.form.get('email', None)
        name = request.form.get('name', None)
        password = request.form.get('password', None)

        form = usersValidate.RegistrationForm(request.form)

        if form.validate():
            try:
                user = UserModel(
                    name=name,
                    password=generate_password_hash(password),
                    email=email
                )
                db.session.add(user)
                db.session.commit()
            except IntegrityError as e:
                error = map(lambda s: s[1:-1], re.findall(r'\'[^\']+\'', str(e)))

                # value, field = error[0], error[1]
                #
                # _return = {
                #     'message': "'" + value + "' is already exists.",
                #     'field': {
                #         'label': getattr(form, field).label.text,
                #         'name': field
                #     }
                # }
                #
                return "err", status.HTTP_400_BAD_REQUEST

            return None, status.HTTP_201_CREATED

        for field, errors in form.errors.items():
            for error in errors:
                _return = {
                    'message': error,
                    'field': getattr(form, field).label.text
                }

                return _return, status.HTTP_400_BAD_REQUEST
