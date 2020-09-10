#!/usr/bin/python3
"""[methods for users routing]
"""
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify, abort, request
from models.user import User


@app_views.route('/users', strict_slashes=False)
def indexUser():
    """indexUser
    """
    lista = []
    value = storage.all("User").values()
    for x in value:
        lista.append(x.to_dict())
    return jsonify(lista)


@app_views.route('/users/<user_id>', strict_slashes=False)
def findUser(user_id):
    """findUser
    """
    value = storage.all("User").values()
    if user_id is not None:
        for x in value:
            if x.id == user_id:
                return jsonify(x.to_dict())
    abort(404)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def updateUser(user_id=None):
    """updateUser
    """
    user = storage.get("User", user_id)
    if user:
        reqq = request.get_json()
        if reqq is None:
            abort(400, "Not a JSON")
        for k, v in reqq.items():
            if k in ['id', 'email', 'created_at', 'updated_at']:
                pass
            setattr(user, k, v)
        storage.save()
        return jsonify(user.to_dict())
    abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteUser(user_id):
    """deleteUser
    """
    user = storage.get("User", user_id)
    if user:
        storage.delete(user)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def saveUser():
    """saveUser
    """
    reqq = request.get_json()
    if reqq is None:
        abort(400, "Not a JSON")
    elif "email" not in reqq.keys():
        abort(400, "Missing email")
    elif "password" not in reqq.keys():
        abort(400, "Missing password")
    else:
        nUser = User(**reqq)
        storage.new(nUser)
        storage.save()
        return jsonify(nUser.to_dict()), 201
