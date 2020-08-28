from flask import Flask
from services.database import init_db

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/kanjinary'

init_db(app)

import controllers

if __name__ == '__main__':
    app.run(debug=True)