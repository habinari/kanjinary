
/*
------------------------------------------------------
------------------ USEFULL METHODS -------------------
------------------------------------------------------
*/

const createDirectoryIfNotExist = path => {
    const fs = require('fs')
    if (!fs.existsSync(path)){
        fs.mkdirSync(path);
    }
}

const saveJsonData = (path, fileName, object) => {
    const fs = require('fs');
    const dir = path + fileName + '.json'
    const jsonData = JSON.stringify(object)
    fs.writeFile(dir, jsonData, function (err) {
        if (err) {
            console.log(err);
        }
    });
}

/*
------------------------------------------------------
---------------------- CONST -------------------------
------------------------------------------------------
*/

const BASE_PATH = './docs/static/'

const KANJI_PATH = BASE_PATH + 'kanji/'
const LEVEL_PATH = BASE_PATH + 'lvl/'

/*
------------------------------------------------------
----------------------- MAIN -------------------------
------------------------------------------------------
*/

const allKanjis = require('./static/all.json')
createDirectoryIfNotExist(BASE_PATH)

// Save all kanji
createDirectoryIfNotExist(KANJI_PATH)
allKanjis.forEach(kanji => saveJsonData(KANJI_PATH, kanji.ideogram, kanji))

// Add all lvls to data struct
let allLevels = []

allKanjis.forEach(kanji => {
    let lvl = allLevels.find(lvl => lvl.name == kanji.lvl)
    if(lvl)
        lvl.kanjis.push(kanji.ideogram)
    else 
        allLevels.push({
            name: kanji.lvl,
            kanjis: [kanji.ideogram]
        })
})

// Save all lvls
createDirectoryIfNotExist(LEVEL_PATH)
saveJsonData(LEVEL_PATH, 'all', allLevels)
allLevels.forEach(lvl => saveJsonData(LEVEL_PATH, lvl.name, lvl))









