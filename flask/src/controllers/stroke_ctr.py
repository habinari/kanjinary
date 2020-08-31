from __main__ import app
from flask import jsonify
from models.stroke import find_one

@app.route('/api/stroke/<stroke>', methods=['GET'])
def search_kanji_refs_by_stroke_num(stroke):
    stroke = int(stroke)
    stroke_data = find_one({ 'strokes': stroke })
    return jsonify(stroke_data['kanjis'] if stroke_data else [])

