# -*- coding: utf-8 -*-
import datetime

from wtforms import Form, IntegerField, validators


class AddSchoolForm(Form):
    admission_year = IntegerField('Admission Year', [
        validators.DataRequired(),
        validators.NumberRange(min=1990, max=datetime.date.today().year)
    ])
    graduation_year = IntegerField('Graduation Year', [
        validators.DataRequired(),
        validators.NumberRange(min=1990, max=datetime.date.today().year + 10)
    ])
