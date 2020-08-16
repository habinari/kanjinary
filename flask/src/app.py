from flask import Flask, request, jsonify
from models.kanji import find
from services.database import init_db

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/kanjinary'

init_db(app)

@app.route('/api/kanji', methods=['GET'])
def search():
    return jsonify(
        find({})
    )

if __name__ == '__main__':
    app.run(debug=True)