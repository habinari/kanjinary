import json
import io
import os

all_kanjis = []

# Create static directory if not exist
directory = './docs/static/'
try:
    os.stat(directory)
except:
    os.mkdir(directory)

# Load all data
with open('./static/all.json') as all_data:  
    data = json.load(all_data)
    for kanji in data:
        all_kanjis.append(kanji)


# Create a directory for kanjis if not exists
kanji_directory = './docs/static/kanji/'
try:
    os.stat(kanji_directory)
except:
    os.mkdir(kanji_directory)

# Save all kanji as individual json file
index = 0
for kanji in all_kanjis:
    with io.open(kanji_directory + kanji['kanji'] + '.json', 'w', encoding='utf8') as outfile:
        kanji['id'] = index
        index += 1
        json.dump(kanji, outfile, indent=4, ensure_ascii=False)

# Get all kanji character order by level (lists)
all_levels = []
for kanji in all_kanjis:
    level_already_crated = False
    for level in all_levels:
        if level['name'] == kanji['lvl']:
            level['kanjis'].append(kanji['kanji'])
            level_already_crated = True
    if not level_already_crated:
        level = {}
        level['name'] = kanji['lvl']
        level['kanjis'] = []
        level['kanjis'].append(kanji['kanji'])
        all_levels.append(level)

# Create a directory for levels if not exists
lvl_directory = './docs/static/lvl/'
try:
    os.stat(lvl_directory)
except:
    os.mkdir(lvl_directory)

# Write all lvls
with io.open(lvl_directory + 'all.json', 'w', encoding='utf8') as outfile:
    json.dump(all_levels, outfile, indent=4, ensure_ascii=False)

# Write all levels individually
index = 0
for level in all_levels:
    with io.open(lvl_directory + level['name'] + '.json', 'w', encoding='utf8') as outfile:
        level['id'] = index
        index += 1
        json.dump(level, outfile, indent=4, ensure_ascii=False)

    
    
    

    

