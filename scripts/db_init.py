import json
from pymongo import MongoClient 

try: 
    conn = MongoClient() 
    print("MongoDB Connection success.") 
except:   
    print("Could not connect to MongoDB.") 

mongodb = conn.kanjinary

with open('./static/all.json', 'r') as read_file:
    data = json.load(read_file)

# --- save all kanjis ---
mongodb['kanjis'].drop()
for kanji_data in data:
    mongodb.kanjis.insert_one(kanji_data)
    
# --- save kanjis by radicals ---
mongodb['radicals'].drop()
radicals = {}
for kanji_data in data:
    radical = kanji_data['radical']
    if not radical in radicals:
        radicals[radical] = []
    radicals[radical].append(kanji_data['ideogram'])

for key, value in radicals.items():
    mongodb.radicals.insert_one({
        'ideogram': key,
        'kanjis': value
    })
radicals = None

# --- save kanjis by stroke numer ---
mongodb['strokes'].drop()
strokes = {}
for kanji_data in data:
    stroke_num = kanji_data['strokes']
    if not stroke_num in strokes:
        strokes[stroke_num] = []
    strokes[stroke_num].append(kanji_data['ideogram'])

for key, value in strokes.items():
    mongodb.strokes.insert_one({
        'strokes': key,
        'kanjis': value
    })
strokes = None

# --- save kanjis by parts of kanji ---
mongodb['parts'].drop()
parts = {}
for kanji_data in data:
    for part in kanji_data['parts']:
        if not part in parts:
            parts[part] = []
        parts[part].append(kanji_data['ideogram'])

for key, value in parts.items():
    mongodb.parts.insert_one({
        'ideogram': key,
        'kanjis': value
    })
parts = None