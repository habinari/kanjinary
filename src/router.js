
// Main libraries imports
import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

// View imports
import Home from './views/Home.vue'
import Kanji from './views/Kanji.vue'
import Level from './views/Level.vue'


export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/kanji',
      name: 'kanji',
      component: Kanji
    },
    {
      path: '/lvl',
      name: 'level',
      component: Level
    }
  ]
})
