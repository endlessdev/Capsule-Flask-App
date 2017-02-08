# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app import db, token_auth
from app.models.user_token_model import token_load_with_auth
from app.models.timeline_comment_model import TimelineCommentModel, get_post_comments
from app.modules import capsule
from app.modules.capsule.validate import timeline as timelineValidate
from app.modules.capsule.serialize.timeline import serialize_comment

_URL = '/timeline/<prefix>/comments'


class Comment(Resource):
    @capsule.API
    @token_auth.login_required
    def get(self, prefix):
        try:
            post_id = int(prefix)

            _return = {
                'data': []
            }

            comments = get_post_comments(post_id)

            for comment in comments:
                _return['data'].append(serialize_comment(comment))

            return _return, status.HTTP_200_OK
        except ValueError:
            return "Prefix can only be number.", status.HTTP_400_BAD_REQUEST

    @capsule.API
    @token_auth.login_required
    def post(self, prefix):
        try:
            post_id = int(prefix)

            content = request.form.get('content', None)

            user_id = token_load_with_auth(request.headers['Authorization'])['user_id']

            form = timelineValidate.CommentForm(request.form)

            if form.validate():
                post = TimelineCommentModel(
                    user_id=user_id,
                    post_id=post_id,
                    content=content
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

                    return _return, status.HTTP_400_BAD_REQUEST
        except ValueError:
            return "Prefix can only be number.", status.HTTP_400_BAD_REQUEST