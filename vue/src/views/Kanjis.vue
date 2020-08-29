<template>
    <div id="kanjis">
        <div class="columns is-centered">
            <div class="column is-10">
                <Kanji v-bind:kanji="kanji"/>
            </div>
        </div>
    </div>
</template>

<script>

import Kanji from '@/components/Kanji.vue'

const KANJI_PATH = 'https://www.javierparada.dev/kanjinary/api/kanji/'

export default {
    name: 'kanjis',

    components: {
        Kanji
    },

    data: function() {
        return {
            test: 'Test kanjis',

            kanji: {}
        }
    },

    beforeMount: function() {
        this.loadKanji()
    },

    methods: {
        loadKanji: function() {
            const kanjiReference = this.$route.params.kanji
            var vueCtx = this
            var axios = require('axios')
            axios.get(KANJI_PATH + kanjiReference)
                .then(function (response) {
                  vueCtx.kanji = response.data
                })
                .catch(function (error) {
                    alert('ERROR')
                })
        }
    }
}
</script>

<style lang="sass">

</style>
