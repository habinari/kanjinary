<template>
  <div id="app">
    <div id="nav">

      <section class="hero is-info is-medium">
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
                      <li class="is-active"><a>Inicio</a></li>
                      <li><a>Niveles</a></li>
                      <li><a>Buscar</a></li>
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
            <h1 class="title">
              Bienvenido a Kanjinary
            </h1>
            <h2 class="subtitle">
              Kanjinary es una base de datos de kanjis hecha por y para estudiantes de japonés.
            </h2>
          </div>
        </div>
      </section>

      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'nav',
  el: '#nav',
  data: function() {
    return {
      test: 'Nav test!'
    }
  }
}
</script>


<style lang="scss">
  @import '/../node_modules/bulma/bulma.sass';
</style>
