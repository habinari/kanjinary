<template>
    <section class="container">
        <div class="columns">
            <div class="column has-text-centered m-t-xl">
                <h1 class="is-size-3 title">{{name}}</h1>
            </div>
        </div>
        <div class="columns is-centered">
            <div v-for="kanji in kanjis" :key="kanji" class="column is-1">
                <router-link v-bind:to="`/kanji/${kanji}`">
                    <p class="is-size-3 has-text-centered has-text-dark">
                      {{kanji}}
                    </p>
                </router-link>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'level',

    data: function() {
        return {
            test: 'Test level!',
        }
    },

    props: {
        name: String,
        kanjis: Array
    }
}
</script>

<style lang="sass">

</style>


