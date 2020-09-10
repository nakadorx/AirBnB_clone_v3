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


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def counter():
    """
    hamammet hammamet
    """
    return jsonify({"amenities": storage.count('Amenity'),
                    "cities": storage.count('City'),
                    "places": storage.count('Place'),
                    "reviews": storage.count('Review'),
                    "states": storage.count('State'),
                    "users": storage.count('User')})
