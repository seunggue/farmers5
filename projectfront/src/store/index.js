import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import sns from './modules/sns'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    auth,
    sns,
  }
})
