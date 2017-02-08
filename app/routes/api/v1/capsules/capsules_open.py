# -*- coding: utf-8 -*-
from flask import json
from flask import request
from flask_api import status
from flask_restful import Resource

from app import token_auth, db
from app.models.capsule_model import get_capsules_by_id
from app.models.user_capsule_open import UserCapsuleOpenModel, get_requested_friends_num
from app.models.user_capsule_model import get_users_num_by_capsule_id
from app.modules import capsule
from geopy.distance import great_circle, vincenty

_URL = '/capsules/<prefix>/open'


class CapsulesOpen(Resource):
    @capsule.API
    @token_auth.login_required
    def post(self, prefix):
        capsule = get_capsules_by_id(prefix)
        capsule_geo = (capsule.latitude, capsule.longitude)
        current_geo = (request.form.get('latitude', 0), request.form.get('longitude', 0))
        user_id = request.form.get('user_id', 0)

        distance = vincenty(capsule_geo, current_geo).meters

        if distance <= 30:
            user_capsule_open = UserCapsuleOpenModel(
                user_id=user_id,
                capsule_id=capsule.id
            )

            db.session.add(user_capsule_open)
            db.session.commit()

            capsule_friends_num = get_capsules_by_id(capsule.id)
            requested_friends_num = get_requested_friends_num(capsule.id)

            if capsule_friends_num == requested_friends_num:
                return "Unlocked capsule", status.HTTP_200_OK
            else:
                return "Not enough people to unlock", status.HTTP_400_BAD_REQUEST

        else:
            return "Out of range", status.HTTP_400_BAD_REQUEST
