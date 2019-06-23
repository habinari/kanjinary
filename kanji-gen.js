
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
const KUN_PATH = BASE_PATH + 'kunyomi/'
const ON_PATH = BASE_PATH + 'onyomi/'

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


// Add all kunyomis to data struct
let allKunyomis = []

allKanjis.forEach(kanji => {
    kanji.kunyomi.forEach(yomi => {
        yomi = yomi.replace('.','')
        let kun = allKunyomis.find(kun => kun.kanas == yomi)
        if(kun)
            kun.kanjis.push(kanji.ideogram)
        else 
            allKunyomis.push({
                kanas: yomi,
                kanjis: [kanji.ideogram]
            })
    })
})

// Save all kunyomis
createDirectoryIfNotExist(KUN_PATH)
saveJsonData(KUN_PATH, 'all', allKunyomis)
allKunyomis.forEach(yomi => saveJsonData(KUN_PATH, yomi.kanas, yomi))


// Add all onyomis to data struct
let allOnyomis = []

allKanjis.forEach(kanji => {
    kanji.onyomi.forEach(yomi => {
        let on = allOnyomis.find(on => on.kanas == yomi)
        if(on)
            on.kanjis.push(kanji.ideogram)
        else 
            allOnyomis.push({
                kanas: yomi,
                kanjis: [kanji.ideogram]
            })
    })
})

// Save all kunyomis
createDirectoryIfNotExist(ON_PATH)
saveJsonData(ON_PATH, 'all', allOnyomis)
allOnyomis.forEach(yomi => saveJsonData(ON_PATH, yomi.kanas, yomi))
