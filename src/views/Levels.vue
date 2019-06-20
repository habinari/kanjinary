<template>
    <div id="levels">

        <div v-for="lvl in levels" :key="lvl.name">
            <Level v-bind:name="lvl.name" v-bind:kanjis="lvl.kanjis" />
        </div>
    </div>
</template>

<script>

const LVL_PATH = 'https://www.kabi404.dev/Kanjinary/static/lvl/all.json'

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
            var vueCtx = this
            var axios = require('axios')
            axios.get(LVL_PATH)
                .then(function (response) {
                  vueCtx.levels = response.data
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

