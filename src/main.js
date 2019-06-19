import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

import { library } from '@fortawesome/fontawesome-svg-core'
import { faCoffee, faUsers, faUnlockAlt } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faCoffee)
library.add(faUnlockAlt)
library.add(faUsers)

Vue.component('font-awesome-icon', FontAwesomeIcon)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
