
// Main libraries imports
import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

// View imports
import Home from './views/Home.vue'
import Kanjis from './views/Kanjis.vue'
import Levels from './views/Levels.vue'
import Search from './views/Search.vue'


export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/kanji/:kanji',
      name: 'kanjis',
      component: Kanjis
    },
    {
      path: '/lvl',
      name: 'levels',
      component: Levels
    },
    {
      path: '/search',
      name: 'search',
      component: Search
    }
  ]
})
