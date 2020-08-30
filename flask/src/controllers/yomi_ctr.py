from __main__ import app
from flask import jsonify
from models.yomi import find_one

@app.route('/api/yomi/<yomi_type>/<yomi>', methods=['GET'])
def search_one_kunyomi(yomi_type, yomi):
    yomi = find_one({
        'yomi': yomi,
        'type': yomi_type
    })
    return jsonify(yomi['kanjis'] if yomi else [])

