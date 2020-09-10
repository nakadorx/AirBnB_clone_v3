#!/usr/bin/python3
"""[methods for amenities routing]
"""
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify, abort, request
from models.amenity import Amenity


@app_views.route('/amenities', strict_slashes=False)
def indexAm():
    """indexAm
    """
    lst = []
    val = storage.all("Amenity").values()
    for obj in val:
        lst.append(obj.to_dict())
    return jsonify(lst)


@app_views.route('/amenities/<amenity_id>', strict_slashes=False)
def findAm(amenity_id):
    """findAm
    """
    val = storage.all("Amenity").values()
    if amenity_id is not None:
        for obj in val:
            if obj.id == amenity_id:
                return jsonify(obj.to_dict())
    abort(404)


@app_views.route('/amenities',
                 methods=['POST'],
                 strict_slashes=False)
def SaveAmenoty():
    """SaveAmenoty
    """
    reqq = request.get_json()
    if reqq is None:
        abort(400, "Not a JSON")
    elif "name" not in reqq.keys():
        abort(400, "Missing name")
    else:
        new_amenity = Amenity(**reqq)
        storage.new(new_amenity)
        storage.save()
        return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def DeteleAmenity(amenity_id):
    """DeteleAmenity
    """
    delt = storage.get("Amenity", amenity_id)
    if delt:
        storage.delete(delt)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'],
                 strict_slashes=False)
def UpdateAmenity(amenity_id=None):
    """UpdateAmenity
    """
    upd = storage.get("Amenity", amenity_id)
    if upd:
        reqq = request.get_json()
        if reqq is None:
            abort(400, "Not a JSON")
        for key, value in reqq.items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            setattr(upd, key, value)
        storage.save()
        return jsonify(upd.to_dict())
    abort(404)
