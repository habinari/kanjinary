from typing import List, Optional
from marshmallow import Schema, fields, post_load
from flask_pymongo import PyMongo
from services.database import mongo

from models.base_model import BaseModel

def find(search_dict={}) -> List['Kanji']:
    return list(mongo.db.kanjis.find(search_dict, {'_id': False}))

class Kanji(BaseModel):
    def __init__(self, ideogram, kunyomi, onyomi, parts, radical, strokes, lvl):
        self.ideogram = ideogram
        self.kunyomi = kunyomi
        self.onyomi = onyomi
        self.parts = parts

class KanjiSchema(Schema):
    ideogram = fields.String()
    kunyomi = fields.List(fields.String())
    onyomi = fields.List(fields.String())
    parts = fields.List(fields.String())
    radical = fields.String()
    strokes = fields.Integer()
    lvl = fields.String()

    @post_load
    def make_kanji(self, data, **kwargs) -> Kanji:
        return Kanji(**data)