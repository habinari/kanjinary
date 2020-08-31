from typing import List, Optional
from marshmallow import Schema, fields, post_load
from flask_pymongo import PyMongo
from services.database import mongo

from models.base_model import BaseModel


def find(search_dict={}) -> List['Strokes']:
    return list(mongo.db.strokes.find(search_dict, {'_id': False}))


def find_one(search_dict={}) -> List['Strokes']:
    print(search_dict)
    return mongo.db.strokes.find_one(search_dict, {'_id': False})


class Stroke(BaseModel):
    def __init__(self, strokes, kanjis):
        self.strokes = strokes
        self.kanjis = kanjis


class StrokeSchema(Schema):
    strokes = fields.Integer()
    kanjis = fields.List(fields.String())
