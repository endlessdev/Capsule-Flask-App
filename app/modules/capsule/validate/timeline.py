# -*- coding: utf-8 -*-
from wtforms import Form, StringField, validators, FloatField


class PostForm(Form):
    title = StringField('Title', [
        validators.DataRequired(),
        validators.Length(min=5)
    ])
    content = StringField('Content', [
        validators.DataRequired(),
        validators.Length(min=10)
    ])
    latitude = FloatField('Latitude', [
        validators.DataRequired()
    ])
    longitude = FloatField('Longitude', [
        validators.DataRequired()
    ])


class CommentForm(Form):
    content = StringField('Content', [
        validators.DataRequired(),
        validators.Length(min=10)
    ])
