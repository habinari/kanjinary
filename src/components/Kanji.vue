<template>
    <section class="container has-text-centered m-t-lg">
        <div class="columns">
            <div class="column">
                <h1 class="title is-size-1">{{kanji.ideogram}}</h1>
            </div>
        </div>

        <div class="columns">
            <div class="is-offset-2 column is-3 has-text-right">
                <p class="is-size-5">Kunyomi:</p>
            </div>
            <div class="column is-4 has-text-left">
                <p class="is-size-5">
                    <span v-for="yomi in kanji.kunyomi" :key="yomi" class="m-l-md">{{yomi}}</span>
                </p>
            </div>
        </div>

        <div class="columns">
            <div class="is-offset-2 column is-3 has-text-right">
                <p class="is-size-5">Onyomi:</p>
            </div>
            <div class="column is-4 has-text-left">
                <p class="is-size-5">
                    <span v-for="yomi in kanji.onyomi" :key="yomi" class="m-l-md">{{yomi}}</span>
                </p>
            </div>
        </div>

        <div class="columns is-centered m-t-md">
            <div class="column is-2">
                <p>Radical:</p> {{kanji.radical}}
            </div>
            <div class="column is-2">
                <p>Trazos:</p> {{kanji.strokes}}
            </div>
            <div class="column is-2">
                <p>Nivel:</p> {{kanji.lvl}}
            </div>
        </div>

    </section>
</template>

<script>
export default {
    name: 'kanji',

    props: {
        kanji: Object
    },

    data: function() {
        return {
        }
    }
}
</script>

<style lang="sass">

</style>
