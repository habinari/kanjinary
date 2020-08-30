from __main__ import app
from flask import send_from_directory

@app.route('/')
def get_index():
    return send_from_directory('../static/', 'index.html')

@app.route('/<path:path>')
def get_from_static_folder(path):
    return send_from_directory('../static/', path)