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

# Get all kanji character order by level (lists)
all_levels = []
for kanji in all_kanjis:
    level_already_crated = False
    for level in all_levels:
        if level['name'] == kanji['lvl']:
            level['kanjis'].append(kanji)
            level_already_crated = True
    if not level_already_crated:
        level = {}
        level['name'] = kanji['lvl']
        level['kanjis'] = []
        level['kanjis'].append(kanji)
        all_levels.append(level)

# Write all levels
index = 0
for level in all_levels:
    with io.open('./docs/static/lvl/' + level['name'] + '.json', 'w', encoding='utf8') as outfile:
        level['id'] = index
        index += 1
        json.dump(level, outfile, ensure_ascii=False)

    
    
    

    

