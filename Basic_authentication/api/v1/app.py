#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
<<<<<<< HEAD
=======
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
>>>>>>> 802b8f3c485136156e0c3fb6df2b6dacea68486d


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

<<<<<<< HEAD
if getenv('AUTH_TYPE') == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif getenv('AUTH_TYPE') == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
=======
if os.getenv('AUTH_TYPE') == 'auth':
    auth = Auth()
elif os.getenv('AUTH_TYPE') == 'basic_auth':
>>>>>>> 802b8f3c485136156e0c3fb6df2b6dacea68486d
    auth = BasicAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
<<<<<<< HEAD
def access_denied(error) -> str:
    """
    Uh Uh Uh. You didnt say the magic word
=======
def unauthorized(error) -> str:
    """ Unauthorized handler
>>>>>>> 802b8f3c485136156e0c3fb6df2b6dacea68486d
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
<<<<<<< HEAD
def access_forbidden(error) -> str:
    """
    No cookies for you
=======
def forbidden(error) -> str:
    """ Forbidden handler
>>>>>>> 802b8f3c485136156e0c3fb6df2b6dacea68486d
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
<<<<<<< HEAD
def before_request_handler():
    """before_request handler"""
    excluded = ['/api/v1/status/',
                '/api/v1/unauthorized/',
                '/api/v1/forbidden/']

    if auth is not None and auth.require_auth(request.path, excluded):
        if auth.authorization_header(request) is None:
            abort(401)

        if auth.current_user(request) is None:
            abort(403)
=======
def before_request_func():
    """ Before request handler
    """
    if auth is None:
        return
    path = request.path
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/',
                      '/api/v1/auth_session/login/']
    if not auth.require_auth(path, excluded_paths):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)
>>>>>>> 802b8f3c485136156e0c3fb6df2b6dacea68486d


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
