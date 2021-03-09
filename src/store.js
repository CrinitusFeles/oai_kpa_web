import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    mku: {
      be: {
        pk1: false,
        pk2: false
      },
      bdd: {
        bdd_on: false,
        tk_on: false
      },
      duration: 0
    },
    power: {
      bdd: {
        power_on: false,
        aim_voltage: 0
      },
      be: {
        power_on: false,
        aim_voltage: 0
      }
    },
    dep: {
      voltage: 0,
      period: 1,
      loop_state: false
    }
  },

  getters: {
    GET_MKU_PK1: state => {
      return state.mku.be.pk1
    },
    GET_MKU_PK2: state => {
      return state.mku.be.pk2
    },
    GET_MKU_OFF: state => {
      return state.mku.be.off
    },
    GET_MKU_BDD_ON: state => {
      return state.mku.bdd.bdd_on
    },
    GET_MKU_TK_ON: state => {
      return state.mku.bdd.tk_on
    },
    GET_MKU_DURATION: state => {
      return state.mku.duration
    },

    GET_POWER_BDD_ON: state => {
      return state.power.bdd.power_on
    },
    GET_POWER_BDD_AIM_VOLTAGE: state => {
      return state.power.bdd.aim_voltage
    },
    GET_POWER_BE_ON: state => {
      return state.power.be.power_on
    },
    GET_POWER_BE_AIM_VOLTAGE: state => {
      return state.power.be.aim_voltage
    },

    GET_DEP_VOLTAGE: state => {
      return state.dep.voltage
    },
    GET_DEP_PERIOD: state => {
      return state.dep.period
    },
    GET_DEP_LOOP_STATE: state => {
      return state.dep.loop_state
    }
  },

  mutations: {
    SET_MKU_PK1: (state, payload) => {
      state.mku.be.pk1 = payload
    },
    SET_MKU_PK2: (state, payload) => {
      state.mku.be.pk2 = payload
    },
    SET_MKU_OFF: (state, payload) => {
      state.mku.be.off = payload
    },
    SET_MKU_BDD_ON: (state, payload) => {
      state.mku.bdd.bdd_on = payload
    },
    SET_MKU_TK_ON: (state, payload) => {
      state.mku.bdd.tk_on = payload
    },
    SET_MKU_DURATION: (state, payload) => {
      state.mku.duration = payload
    },

    SET_POWER_BDD_ON: (state, payload) => {
      state.power.bdd.power_on = payload
    },
    SET_POWER_BDD_AIM_VOLTAGE: (state, payload) => {
      state.power.bdd.aim_voltage = payload
    },
    SET_POWER_BE_ON: (state, payload) => {
      state.power.be.power_on = payload
    },
    SET_POWER_BE_AIM_VOLTAGE: (state, payload) => {
      state.power.be.aim_voltage = payload
    },

    SET_DEP_VOLTAGE: (state, payload) => {
      state.dep.voltage = payload
    },
    SET_DEP_PERIOD: (state, payload) => {
      state.dep.period = payload
    },
    SET_DEP_LOOP_STATE: (state, payload) => {
      state.dep.loop_state = payload
    }
  },

  actions: {
    INIT_STATE: async (context, payload) => {
      await Axios.get('http://192.168.31.9:5000/api/view_model').then(x => {
        context.commit('SET_MKU_PK1', x.data.mku.be.pk1_state)
        context.commit('SET_MKU_PK2', x.data.mku.be.pk2_state)
        context.commit('SET_MKU_OFF', x.data.mku.be.off_state)
        context.commit('SET_MKU_BDD_ON', x.data.mku.bdd.bdd_on_state)
        context.commit('SET_MKU_TK_ON', x.data.mku.bdd.tk_on_state)
        context.commit('SET_MKU_DURATION', x.data.mku.imp_duration_ms)
        context.commit('SET_POWER_BDD_ON', x.data.power.bdd.on_state)
        context.commit('SET_POWER_BDD_AIM_VOLTAGE', x.data.power.bdd.aim_voltage)
        context.commit('SET_POWER_BE_ON', x.data.power.be.on_state)
        context.commit('SET_POWER_BE_AIM_VOLTAGE', x.data.power.be.aim_voltage)
        context.commit('SET_DEP_VOLTAGE', x.data.dep.voltage)
        context.commit('SET_DEP_PERIOD', x.data.dep.period)
        context.commit('SET_DEP_LOOP_STATE', x.data.dep.loop_state)
      })
    }
  }
})
