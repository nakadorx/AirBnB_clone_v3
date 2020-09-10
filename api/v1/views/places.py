#!/usr/bin/python3
"""[methods for places routing]
"""
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify, abort, request
from models.place import Place


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'],
                 strict_slashes=False)
def indexPlace(city_id=None):
    """indexPlace
    """
    x = storage.get("City", city_id)
    if x:
        return jsonify([place.to_dict() for place in x.places])
    abort(404)


@app_views.route('/places/<place_id>',
                 methods=['GET'],
                 strict_slashes=False)
def findPlace(place_id):
    """findPlace
    """
    place = storage.all("Place").values()
    if place_id is not None:
        for x in place:
            if x.id == place_id:
                return jsonify(x.to_dict())
    abort(404)


@app_views.route('/places/<place_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def deletePlace(place_id):
    """deletePlace
    """
    place = storage.get("Place", place_id)
    if place:
        storage.delete(place)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'],
                 strict_slashes=False)
def savePlace(city_id):
    """savePlace
    """
    ct = storage.get("City", city_id)
    if ct:
        cont = request.get_json()
        if not cont:
            abort(400, "Not a JSON")
        if 'user_id' not in cont:
            abort(400, "Missing user_id")
        user = storage.get("User", cont['user_id'])
        if not user:
            abort(404)
        if 'name' not in cont:
            abort(400, "Missing name")
        cont['city_id'] = ct.id
        place = Place(**cont)
        storage.new(place)
        storage.save()
        return jsonify(place.to_dict()), 201
    abort(404)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def updatePlace(place_id=None):
    """updatePlace
    """
    place = storage.get("Place", place_id)
    if place:
        reqq = request.get_json()
        if reqq is None:
            abort(400, "Not a JSON")
        for key, value in reqq.items():
            if key in ['id', 'user_id', 'city_id', 'created_at',
                     'updated_at']:
                pass
            setattr(place, key, value)
        storage.save()
        return jsonify(place.to_dict())
    abort(404)
