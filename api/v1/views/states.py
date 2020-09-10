#!/usr/bin/python3
"""cmnt
"""
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify, abort, request
from models.state import State


@app_views.route('/states', strict_slashes=False)
def indexSt():
    """index
    """
    res = []
    for state in storage.all("State").values():
        res.append(state.to_dict())
    return jsonify(res)


@app_views.route('/states/<state_id>', strict_slashes=False)
def findSt(state_id):
    """find
    """
    states = storage.all("State").values()
    if state_id is not None:
        for x in states:
            if x.id == state_id:
                return jsonify(x.to_dict())
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def saveSt():
    """saveSt
    """
    reqq = request.get_json()
    if reqq is None:
        abort(400, "Not a JSON")
    elif "name" not in reqq.keys():
        abort(400, "Missing name")
    else:
        new_state = State(**reqq)
        storage.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def updateSt(state_id=None):
    """updateSt
    """
    updateS = storage.get("State", state_id)
    if updateS is None:
        abort(404)
    reqq = request.get_json()
    if reqq is None:
        abort(400, "Not a JSON")
    for key, value in reqq.items():
        if key in ['id', 'created_at', 'updated_at']:
            pass
        setattr(updateS, key, value)
    storage.save()
    return jsonify(updateS.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteSt(state_id):
    """delete
    """
    deleteSt = storage.get("State", state_id)
    if deleteSt:
        storage.delete(deleteSt)
        storage.save()
        return jsonify({})
    abort(404)
