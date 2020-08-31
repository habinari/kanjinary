from __main__ import app
from flask import jsonify
from models.yomi import find_one

@app.route('/api/syllabary/<syllabary>/<yomi>', methods=['GET'])
def search_kanji_refs_by_yomi(syllabary, yomi):
    yomi = find_one({
        'yomi': yomi,
        'type': syllabary
    })
    return jsonify(yomi['kanjis'] if yomi else [])

