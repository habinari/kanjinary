from __main__ import app
from flask import request, jsonify
from models.kanji import find
from decorators.verify_query_params import verify_query_params
from decorators.build_query import build_query

@app.route('/api/kanji', methods=['GET'])
@verify_query_params("kanji-search")
@build_query
def search(query={}):
    return jsonify(find(query))