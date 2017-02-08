# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from app.config import DATABASE, TOKEN_SCHEME


# API SERVER APPLICATION
app = Flask(__name__)
CORS(app)
api = Api(app)


# DATABASE
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# BASIC AUTH AUTHENTICATION
basic_auth = HTTPBasicAuth()


# TOKEN AUTH AUTHENTICATION
token_auth = HTTPTokenAuth(scheme=TOKEN_SCHEME)
