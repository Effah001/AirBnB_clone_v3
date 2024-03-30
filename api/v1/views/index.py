#!/usr/bin/python3
"""
endpoint(route) status
"""
from flask import Flask
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """Returns a JSON status"""
    return jsonify{"status": "OK"}
