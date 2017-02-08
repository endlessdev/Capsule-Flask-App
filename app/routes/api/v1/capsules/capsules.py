# -*- coding: utf-8 -*-
from flask import json
from flask import request
from flask_api import status
from flask_restful import Resource

from app import token_auth, db
from app.config import DEFAULT_URL
from app.models.capsule_model import CapsuleModel, get_capsules
from app.models.user_activities import UserActivitiesModel
from app.models.user_capsule_model import UserCapsuleModel
from app.models.user_model import get_user_with_email, get_user_with_id
from app.models.user_token_model import token_is_auth, token_load_with_auth
from app.modules import capsule
from app.modules.capsule.serialize.capsule import serialize_capsule

_URL = '/capsules'


class Capsules(Resource):
    @capsule.API
    @token_auth.login_required
    def post(self):
        title = request.form.get('title', None)
        latitude = request.form.get('latitude', None)
        longitude = request.form.get('longitude', None)
        friends = request.form.getlist('friends[]')
        content = request.form.get('content', None)
        school_id = request.form.get('school_id', None)

        # Create capsule data
        capsule = CapsuleModel(
            user_id=token_load_with_auth(request.headers['Authorization'])['user_id'],
            latitude=latitude,
            longitude=longitude,
            title=title,
            content=content,
            school_id=school_id,
        )

        # Add Capsule data
        db.session.add(capsule)
        db.session.commit()

        _capsule = CapsuleModel.query.order_by(CapsuleModel.id.desc()).first()
        _capsule_id = _capsule.id

        for friend in friends:
            print(friend)
            user_capsule = UserCapsuleModel(
                capsule_id=_capsule_id,
                user_id=get_user_with_email(friend).id
            )
            db.session.add(user_capsule)
            db.session.commit()

        user_info = get_user_with_id(token_load_with_auth(request.headers['Authorization'])['user_id'], )
        # Save to UserActivities table
        print('_capsule.title: ', _capsule.title[2:])
        user_activities = UserActivitiesModel(
            user_id=user_info.id,
            content='%(user_name)s이 새로운 타임캡슐인 %(capsule_name)s을 만들었습니다!'% {
                'user_name': user_info.name,
                'capsule_name': _capsule.title[2:]
            }
        )
        db.session.add(user_activities)
        db.session.commit()

        return serialize_capsule(_capsule), status.HTTP_201_CREATED

    @capsule.API
    @token_auth.login_required
    def get(self):

        _return = {
            'data': []
        }

        capsules = get_capsules()

        for capsule in capsules:
            _return['data'].append(serialize_capsule(capsule))

        return _return, status.HTTP_200_OK
