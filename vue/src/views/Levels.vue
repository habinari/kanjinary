<template>
    <div id="levels">
        <div v-for="lvl in levels" :key="lvl.name">
            <Level v-bind:name="lvl.name" v-bind:kanjis="lvl.kanjis" />
        </div>
    </div>
</template>

<script>

const LVL_PATH = 'https://www.javierparada.dev/kanjinary/static/lvl/'

import Level from '@/components/Level.vue'

export default {
    name: 'Levels',

    components: {
        Level
    },

    data: function() {
        return {
            test: 'Test Level!!',

            lvlReference: '',

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
            if(!this.lvlReference)
                this.lvlReference = this.$route.params.lvl
            var vueCtx = this
            var axios = require('axios')
            axios.get(LVL_PATH + vueCtx.lvlReference)
                .then(function (response) {
                  vueCtx.levels = response.data
                  if(vueCtx.lvlReference != 'all')
                    vueCtx.levels = [vueCtx.levels]
                })
                .catch(function (error) {
                    alert('ERROR')
                });
        }
    },

    beforeRouteUpdate: function(to, from, next) {
        this.lvlReference = to.params.lvl
        this.loadLevels();
        next();
    }
}
</script>

<style lang="sass">

</style>

