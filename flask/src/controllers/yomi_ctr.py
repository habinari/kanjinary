from __main__ import app
from flask import request, jsonify
from models.yomi import find_one
from decorators.verify_query_params import verify_query_params
from decorators.build_query import build_query

@app.route('/api/yomi/<yomi_type>/<yomi>', methods=['GET'])
def search_one_kunyomi(yomi_type, yomi):
    yomi = find_one({
        'yomi': yomi,
        'type': yomi_type
    })
    return jsonify(
        yomi['kanjis'] if yomi != None else []
    )

