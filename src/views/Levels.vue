<template>
    <div id="levels">
        <div v-for="lvl in levels" :key="lvl.name">
            <Level v-bind:name="lvl.name" v-bind:kanjis="lvl.kanjis" />
        </div>
    </div>
</template>

<script>

const LVL_PATH = 'https://www.kabi404.dev/Kanjinary/static/lvl/'

import Level from '@/components/Level.vue'

export default {
    name: 'Levels',

    components: {
        Level
    },

    data: function() {
        return {
            test: 'Test Level!!',

            levels: [
                {

                }
            ]
        }
    },

     beforeMount: function() {
        this.loadLevels()
    },

    methods: {
        loadLevels: function() {
            const lvlReference = this.$route.params.lvl
            var vueCtx = this
            var axios = require('axios')
            axios.get(LVL_PATH + lvlReference + '.json')
                .then(function (response) {
                  vueCtx.levels = response.data
                  if(lvlReference != 'all')
                    vueCtx.levels = [vueCtx.levels]
                })
                .catch(function (error) {
                    alert('ERROR')
                });
        }
    }
}
</script>

<style lang="sass">

</style>

