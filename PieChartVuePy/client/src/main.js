import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Chartkick from 'vue-chartkick'
import Chart from 'chart.js'
import Dropdown from './components/Dropdown.vue'

Vue.config.productionTip = false
Vue.use(Chartkick.use(Chart))
new Vue({
  router,
  components: { 'my-dropdown': Dropdown },
  render: h => h(App),
}).$mount('#app')
