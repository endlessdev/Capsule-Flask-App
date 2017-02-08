# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app import db, token_auth
from app.models.school_model import get_school
from app.models.user_token_model import token_load_with_auth
from app.models.user_school_model import UserSchoolModel, get_user_school
from app.modules import capsule
from app.modules.capsule.validate import school as schoolValidate
from app.modules.capsule.serialize.school import serialize_school

_URL = '/schools/<prefix>'


class School(Resource):
    @capsule.API
    @token_auth.login_required
    def get(self, prefix):
        try:
            school_id = int(prefix)

            school = get_school(school_id)

            if school is not None:
                return serialize_school(school), status.HTTP_200_OK

            return "It does not exist.", status.HTTP_404_NOT_FOUND
        except ValueError:
            return "Prefix can only be number.", status.HTTP_400_BAD_REQUEST

    @capsule.API
    @token_auth.login_required
    def post(self, prefix):
        try:
            school_id = int(prefix)
            user_id = token_load_with_auth(request.headers['Authorization'])['user_id']

            school = get_school(school_id)

            if school is not None:
                admission_year = request.form.get('admission_year', None)
                graduation_year = request.form.get('graduation_year', None)

                form = schoolValidate.AddSchoolForm(request.form)

                if form.validate():
                    user_schools = get_user_school(user_id)

                    for user_school in user_schools:
                        if user_school.school_id == school_id:
                            return "The school you have already entered.", status.HTTP_400_BAD_REQUEST

                    user_school = UserSchoolModel(
                        user_id=user_id,
                        school_id=school_id,
                        admission_year=admission_year,
                        graduation_year=graduation_year
                    )
                    db.session.add(user_school)
                    db.session.commit()

                    return None, status.HTTP_200_OK

                for field, errors in form.errors.items():
                    for error in errors:
                        _return = {
                            'message': error,
                            'field': getattr(form, field).label.text
                        }

                        return _return, status.HTTP_400_BAD_REQUEST

            return "It does not exist.", status.HTTP_404_NOT_FOUND
        except ValueError:
            return "Prefix can only be number.", status.HTTP_400_BAD_REQUEST
