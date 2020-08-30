from __main__ import app
from flask import jsonify
from models.radical import find_one

@app.route('/api/radical/<radical>', methods=['GET'])
def search_kanji_refs_by_radical(radical):
    radical_data = find_one({ 'ideogram': radical })
    return jsonify(radical_data['kanjis'] if radical_data else [])

