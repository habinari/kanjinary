from jsonschema import validate
from flask import request


def build_query(special_types=[]):
    def decorator(f):
        def decorated_function_wrapper(**kwargs):
            query = request.args.to_dict()
            for key, value in special_types:
                if value == 'number' and key in query:
                    try:
                        query[key] = int(query[key])
                    except:
                        pass
            kwargs['query'] = query
            return f(**kwargs)
        return decorated_function_wrapper
    return decorator
