# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app import db, token_auth
from app.config import DEFAULT_URL
from app.models.timeline_model import TimelineModel, get_timeline
from app.models.user_token_model import token_load_with_auth
from app.modules import capsule
from app.modules.capsule.validate import timeline as timelineValidate
from app.modules.capsule.serialize.timeline import serialize_post

_URL = '/timeline'


class Timelines(Resource):
    @capsule.API
    @token_auth.login_required
    def get(self):
        page = request.args.get('page', 0, type=int)
        limit = request.args.get('limit', 10, type=int)
        order = request.args.get('order', 'desc')

        _return = {
            'paging': {
                'previous': '%s%s?page=%d&limit=%d&order=%s' % (
                    DEFAULT_URL, request.path, page if page < 1 else page - 1, limit, order
                ),
                'next': '%s%s?page=%d&limit=%d&order=%s' % (
                    DEFAULT_URL, request.path, page + 1, limit, order
                )
            },
            'data': []
        }
        posts = get_timeline(order, page, limit)

        for post in posts:
            _return['data'].append(serialize_post(post))

        return _return, status.HTTP_200_OK

    @capsule.API
    @token_auth.login_required
    def post(self):
        title = request.form.get('title', None)
        content = request.form.get('content', None)
        latitude = request.form.get('latitude', None)
        longitude = request.form.get('longitude', None)

        print('longitude :', longitude)
        user_id = token_load_with_auth(request.headers['Authorization'])['user_id']

        form = timelineValidate.PostForm(request.form)

        if form.validate():
            post = TimelineModel(
                user_id=user_id,
                title=title,
                content=content,
                latitude=latitude,
                longitude=longitude
            )
            db.session.add(post)
            db.session.commit()

            return None, status.HTTP_201_CREATED

        for field, errors in form.errors.items():
            for error in errors:
                _return = {
                    'message': error,
                    'field': getattr(form, field).label.text
                }
                print(_return)
                return _return, status.HTTP_400_BAD_REQUEST
