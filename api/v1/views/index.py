#!/usr/bin/python3
"""
fahras
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review


@app_views.route('/status')
def all_states():
    """
    comntaire comantaire
    """
    return jsonify(status="OK")


@app_views.route('/stats')
def counts():
    """
    hamammet hammamet
    """
    result = {
            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
            }
    return jsonify(result)
