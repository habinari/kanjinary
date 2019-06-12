import json
import io

all_kanjis = []

# Load all data
with open('./data/all.json') as all_data:  
    data = json.load(all_data)
    for kanji in data:
        all_kanjis.append(kanji)

# Save all kanji as individual json file
index = 0
for kanji in all_kanjis:
    with io.open('./docs/static/kanji/' + kanji['kanji'] + '.json', 'w', encoding='utf8') as outfile:  
        kanji['id'] = index
        index += 1
        json.dump(kanji, outfile, ensure_ascii=False)

