from typing import List, Optional
from marshmallow import Schema, fields, post_load
from flask_pymongo import PyMongo
from services.database import mongo

from models.base_model import BaseModel


def find(search_dict={}) -> List['Radicals']:
    return list(mongo.db.radicals.find(search_dict, {'_id': False}))


def find_one(search_dict={}) -> List['Radicals']:
    print(search_dict)
    return mongo.db.radicals.find_one(search_dict, {'_id': False})


class Radical(BaseModel):
    def __init__(self, ideogram, kanjis, type):
        self.ideogram = ideogram
        self.kanjis = kanjis


class RadicalSchema(Schema):
    ideogram = fields.String()
    kanjis = fields.List(fields.String())
