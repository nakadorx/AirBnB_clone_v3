#!/usr/bin/python3
"""
fahras
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def all_states():
    """
    comntaire comantaire
    """
    return jsonify(status="OK")
