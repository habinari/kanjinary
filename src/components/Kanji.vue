<template>
    <section class="container has-text-centered m-t-lg">
        <div class="columns">
            <div class="column">
                <h1 class="title is-size-1">{{kanji.kanji}}</h1>
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
