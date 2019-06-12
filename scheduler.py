import json

all_kanji = []

with open('./data/all.json') as all_data:  
    data = json.load(all_data)
    for kanji in data:
        print('kanji: ' + kanji['kanji'])
        print('Website: ' + kanji['kunyomi'][0])
        print('From: ' + kanji['onyomi'][0])