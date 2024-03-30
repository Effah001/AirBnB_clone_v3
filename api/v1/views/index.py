#!/usr/bin/python3
"""
endpoint(route) status
"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__)


@app_views.route('/status')
def status():
    """Returns a JSON status"""
    return {"status": "OK"}
