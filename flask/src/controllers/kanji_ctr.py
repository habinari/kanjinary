from __main__ import app
from flask import Flask, request, jsonify
from models.kanji import find

@app.route('/api/kanji', methods=['GET'])
def search():
    return jsonify(find())