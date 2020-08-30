from jsonschema import validate
from flask import request
import json
from pathlib import Path


def verify_query_params(schema):
    with open(f'{Path(__file__).parent.absolute()}/../schemas/{schema}.schema.json') as read_file:
        schema = json.load(read_file)

    def decorator(f):
        def decorated_function_wrapper(**kwargs):
            validate(request.args.to_dict(), schema)
            return f(**kwargs)
        return decorated_function_wrapper
    return decorator
