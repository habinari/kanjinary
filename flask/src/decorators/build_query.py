from jsonschema import validate
from flask import request


def build_query(f):
    def decorated_function_wrapper():
        return f(request.args.to_dict())
    return decorated_function_wrapper
