#!/usr/bin/python3
"""cities"""
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify, abort, request


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'],
                 strict_slashes=False)
def indexCity(state_id):
    """indexCity"""
    state = storage.get("State", state_id)
    if state:
        return jsonify([city.to_dict() for city in state.cities])
    abort(404)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def findCity(city_id):
    """findCity"""
    x = storage.get("City", city_id)
    if x:
        return jsonify(x.to_dict())
    abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def deleteCity(city_id):
    """deleteCity"""
    x = storage.get("City", city_id)
    if x:
        storage.delete(x)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def updateCity(city_id):
    """updateCity"""
    x = storage.get("City", city_id)
    if x:
        content = request.get_json()
        if content is None:
            abort(400, "Not a JSON")
        for k, v in content.items():
            if k in ['id', 'state_id', 'created_at', 'updated_at']:
                pass
            setattr(x, k, v)
        storage.save()
        return jsonify(x.to_dict())
    abort(404)


@app_views.route('states/<state_id>/cities',
                 methods=['POST'],
                 strict_slashes=False)
def saveCity(state_id):
    """saveCity"""
    from models.city import City
    st = storage.get("State", state_id)
    if st:
        cont = request.get_json()
        if not cont:
            abort(400, "Not a JSON")
        if 'name' not in cont:
            abort(400, "Missing name")
        cont['state_id'] = st.id
        city = City(**cont)
        storage.new(city)
        storage.save()
        return jsonify(city.to_dict()), 201
    abort(404)
