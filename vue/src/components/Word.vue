<template>
    <div class="box is-fullheight">
        <article class="media">
          <div class="media-content m-l-sm m-r-sm">
            <div class="content">
              <p class="has-text-centered is-size-4">
                <strong>{{word.kotoba}}</strong>
              </p>
              <p class="has-content-justify">
                  Furigana: {{word.reading}}
              </p>
              <p class="has-content-justify">
                  Significados:
                  <span v-for="(meaning, index) in word.meanings.es" :key="index">
                    {{meaning | capitalize}}
                    <span v-if="(index +1) < word.meanings['es'].length">,</span>
                  </span>
              </p>
            </div>
          </div>
        </article>
    </div>
</template>

<script>
export default {
    name: 'word',

    props: {
        word: Object
    },

    data: function() {
        return {
            test: 'Word Test!'
        }
    },

    filters: {
      capitalize: function (value) {
        if (!value) return ''
        value = value.toString()
        return value.charAt(0).toUpperCase() + value.slice(1)
      }
    }
}
</script>

<style lang="sass">

</style>
