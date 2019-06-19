<template>
    <div id="levels">

        <div v-for="lvl in levels" :key="lvl.name">
            <section class="container">
                <div class="columns">
                    <div class="column has-text-centered m-t-lg">
                        <h1 class="is-size-2">{{lvl.name}}</h1>
                    </div>
                </div>
                <div class="columns is-centered">
                    <div v-for="kanji in lvl.kanjis" :key="kanji" class="column is-1">
                        <div class="card">
                            <div class="card-content has-text-centered">
                              <p class="title has-text-centered">
                                {{kanji}}
                              </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>

<script>

const LVL_PATH = 'https://www.kabi404.dev/Kanjinary/static/lvl/all.json'

export default {
    name: 'Levels',

    data: function() {
        return {
            test: 'Test Level!!',

            levels: [
                {

                }
            ]
        }
    },

    mounted: function() {
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

