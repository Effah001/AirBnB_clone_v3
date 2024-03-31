#!/usr/bin/python3
"""Init file for views module"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


# Wildcard import of everything from the index module
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
