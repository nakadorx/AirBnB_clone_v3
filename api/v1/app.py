#!/usr/bin/python3
"""
app file and fuction
"""

from api.v1.views import app_views
from flask import Flask, render_template, jsonify, Response
from models import storage
from os import getenv
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """
    tear down fonction and description
    """
    storage.close()


@app.errorhandler(404)
def handle_error_404(e):
    """
    give me the error 404
    """
    return jsonify(error="Not found"), 404


if __name__ == "__main__":
    """
    climatiseurr fil 16 3wina hashtag
    """
    app.run(host=getenv('HBNB_API_HOST', default='0.0.0.0'),
            port=getenv('HBNB_API_PORT', default=5000),
            threaded=True)
