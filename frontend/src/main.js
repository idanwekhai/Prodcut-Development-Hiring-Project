import Vue from 'vue'
import App from './App.vue'
import router from './router'
// import Buefy from 'buefy'
// import 'buefy/dist/buefy.css'
import $risktypes from './risk-type_model'

Vue.prototype.$risktypes = $risktypes
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
