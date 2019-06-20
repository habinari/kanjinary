<template>
  <div id="app">

    <section class="hero is-info" v-bind:class="{'is-medium': current == 'home'}">
      <!-- Hero head: will stick at the top -->
      <div class="hero-head">
        <nav class="navbar">
          <div class="container">
            <div class="navbar-brand">
              <a class="navbar-item">
                <img src="https://bulma.io/images/bulma-type-white.png" alt="Logo">
              </a>
              <span class="navbar-burger burger" data-target="navbarMenuHeroA">
                <span></span>
                <span></span>
                <span></span>
              </span>
            </div>
            <div id="navbarMenuHeroA" class="navbar-menu">
              <div class="navbar-end">
                <div class="tabs">
                  <ul>
                    <li v-bind:class="{'is-active': current == 'home'}">
                      <router-link to="/">Inicio</router-link>
                    </li>
                    <li v-bind:class="{'is-active': current == 'levels'}">
                      <router-link to="/lvl">Niveles</router-link>
                    </li>
                    <li v-bind:class="{'is-active': current == 'search'}">
                      <router-link to="/search">Buscar</router-link>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </nav>
      </div>
    
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
              to="/lvl" 
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
      startMsg: 'Comenzar por niveles'
    }
  },

  computed: {
    current: function() {
      return this.$route.name
    }
  }

}
</script>


<style lang="scss">
  @import '/../node_modules/bulma/bulma.sass';
  @import '@/styles/space.scss'
</style>
