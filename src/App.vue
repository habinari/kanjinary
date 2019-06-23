<template>
  <div id="app">

    <!-- Hero head: will stick at the top -->
    <nav class="navbar is-info is-fixed-top" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        
        <a class="navbar-item" href="https://bulma.io">
          <img src="https://bulma.io/images/bulma-type-white.png" width="112" height="28">
        </a>

        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <router-link to="/" class="navbar-item" v-bind:class="{'is-active': current == 'home'}">
            Inicio
          </router-link>
          <router-link to="/levels/all" class="navbar-item" v-bind:class="{'is-active': current == 'levels'}">
            Niveles
          </router-link>
          <router-link to="/search" class="navbar-item" v-bind:class="{'is-active': current == 'search'}">
            Buscar
          </router-link>
          
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            
            <div class="field has-addons">
              <div class="control">
                <input class="input is-rounded" type="text" placeholder="Buscar">
              </div>
              <div class="control">
                <a class="button is-link is-rounded">
                  <font-awesome-icon icon="search"/>
                </a>
              </div>
            </div>

          </div>
        </div>
      </div>
    </nav>

    <section class="hero is-info" v-bind:class="{'is-medium': current == 'home'}">
      <!-- Hero content: will be in the middle -->
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="title is-size-2">
            {{title}}
          </h1>
          <h2 v-if="(current == 'home')" class="subtitle">
            {{welcomeMsg}}
          </h2>
          <router-link 
              to="/levels/小学校の１年"
              v-if="(current == 'home')" 
              class="button is-info is-inverted is-outlined">
                {{startMsg}}
          </router-link>
        </div>
      </div>
    </section>

    <router-view/>

    <Footer/>
  </div>
</template>

<script>

import Footer from '@/components/Footer.vue'

export default {
  name: 'app',

  components: {
    Footer
  },

  data: function() {
    return {
      test: 'Nav test!',

      title: '漢字ナリ',
      welcomeMsg: 'Bienvenido a Kanjinary, una base de datos de kanjis hecha por y para estudiantes de japonés.',
      startMsg: 'Comenzar por el primer nivel'
    }
  },

  computed: {
    current: function() {
      return this.$route.name
    }
  },

  methods: {
    burgerToggleEventAdd: function() {
      const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

      if ($navbarBurgers.length > 0) {
        $navbarBurgers.forEach( el => {
          el.addEventListener('click', () => {
          
            const target = el.dataset.target;
            const $target = document.getElementById(target);

            el.classList.toggle('is-active');
            $target.classList.toggle('is-active');
          });
        });
      }
    }
  },

  mounted: function() {
    this.burgerToggleEventAdd()
  }
}
</script>


<style lang="sass">
  @import '/../node_modules/bulma/bulma.sass'
  @import '@/styles/space.scss'

  .tabs
    ul
      border-bottom-color: $info
</style>
