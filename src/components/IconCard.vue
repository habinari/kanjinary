<template>
    <div class="card">
        <div class="card-image has-text-centered">
            <i class=""></i>
        </div>
        <div class="card-content">
            <div class="content">
                <h4>{{title}}</h4>
                <p>{{content}}</p>
                <p><a href="#">{{link}}</a></p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'icon-card',

  data: function() {
    return {
      test: 'Nav icon-card!',
      title: 'title',
      content: 'content',
      link: 'link'
    }
  },

  computed: {
    current: function() {
      return this.$route.name
    }
  }

}
</script>

