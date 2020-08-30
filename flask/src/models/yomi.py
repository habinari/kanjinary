from typing import List, Optional
from marshmallow import Schema, fields, post_load
from flask_pymongo import PyMongo
from services.database import mongo

from models.base_model import BaseModel


def find(search_dict={}) -> List['Yomis']:
    return list(mongo.db.yomis.find(search_dict, {'_id': False}))


def find_one(search_dict={}) -> List['Yomis']:
    print(search_dict)
    return mongo.db.yomis.find_one(search_dict, {'_id': False})


class Kanji(BaseModel):
    def __init__(self, yomi, kanjis, type):
        self.yomi = yomi
        self.kanjis = kanjis
        self.type = type


class KanjiSchema(Schema):
    yomi = fields.String()
    kanjis = fields.List(fields.String())
    type = fields.String()
