import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import { BModal, VBModal, BFormInput } from 'bootstrap-vue'
import VueCookies from 'vue-cookies'

Vue.config.productionTip = false
Vue.use(BootstrapVue)

Vue.use(VueCookies)

Vue.component('b-form-input', BFormInput)
Vue.component('b-modal', BModal)
Vue.directive('b-modal', VBModal)
Vue.$cookies.config('1h')

new Vue({
  render: h => h(App),
}).$mount('#app')
