import Vue from 'vue'
import Router from 'vue-router'
import Vuex from 'vuex'

const routerOptions = [
  { path: '/', component: 'Home' },
  { path: '*', component: 'NotFound' }
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/main_window/${route.component}.vue`)
  }
})

Vue.use(Router)
Vue.use(Vuex)

export default new Router({
  routes,
  mode: 'history'
})
export const store = new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {}
})
