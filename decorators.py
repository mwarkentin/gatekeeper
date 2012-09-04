import os

from functools import wraps
from flask import abort, request


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get('Authorization') != os.environ.get('GATEKEEPER_TOKEN'):
            abort(401)
        return f(*args, **kwargs)
    return decorated_function
