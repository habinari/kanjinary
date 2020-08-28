from jsonschema import validate
from flask import request
import json
import os

def verify_query_params(schema):
    with open(os.path.dirname(__file__) + "/../schemas/" + (schema + '.schema.json'), 'r') as read_file:
        schema = json.load(read_file)
    def decorator(f):
        def decorated_function_wrapper(**kwargs):
            validate(request.args.to_dict(), schema)
            return f(**kwargs)
        return decorated_function_wrapper
    return decorator
