<template>
    <div class="card">
        <div class="card-image has-text-centered has-text-info">
            <font-awesome-icon v-bind:icon="iconRef" class="is-size-1 m-t-lg"/>
        </div>
        <div class="card-content m-t-lg">
            <div class="content has-text-justified">
                <h4>{{title}}</h4>
                <p>{{content}}</p>
                <p><a target="_blank" v-bind:href="href">{{link}}</a></p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'icon-card',

  props: {
      title: String,
      content: String,
      link: String,
      href: String,
      iconRef: String
  },

  data: function() {
    return {
      test: 'Test icon-card!',
    }
  },

  computed: {
    current: function() {
      return this.$route.name
    }
  }

}
</script>

<style lang="sass">
    .card
      height: 100%
</style>


