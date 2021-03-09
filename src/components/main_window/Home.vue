
<template>
    <div  v-if="data_done" class="page_background">
      <!-- <div class="header-bg"> 🚫🔌-->
        <!-- <connect-bar ref="connection_bar_comp"/> -->
      <!-- </div> -->
      <div class="div_top">
        <div class="div_btn"> <tabs class="tabs" ref="tabs_comp"></tabs></div>
        <div class="div_tabs"> <VueLoadingButton name="kek" class="load_btn" @click.native="connect" :loading="isLoading" :styled="false"> Подключиться </VueLoadingButton></div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import tabs from './tabs/tabs'
import ConnectBar from './connect_bar'
import VueLoadingButton from 'vue-loading-button'
export default {
  data () {
    return {
      isLoading: false,
      interval: undefined,
      model_data: {},
      data_done: false
    }
  },
  components: { tabs, ConnectBar, VueLoadingButton },
  methods: {
    update_data () {
      axios.get('http://10.6.1.86:5000/api/view_model')
        .then(x => {
          this.$refs.tabs_comp.update_tabs(x.data)
          // this.$refs.connection_bar_comp.update_status(x.data)
          this.$store.commit('SET_MKU_PK1', x.data.mku.be.pk1_state)
          this.$store.commit('SET_MKU_PK2', x.data.mku.be.pk2_state)
          this.$store.commit('SET_MKU_OFF', x.data.mku.be.off_state)
          this.$store.commit('SET_MKU_BDD_ON', x.data.mku.bdd.bdd_on_state)
          this.$store.commit('SET_MKU_TK_ON', x.data.mku.bdd.tk_on_state)
          this.$store.commit('SET_MKU_DURATION', x.data.mku.imp_duration_ms)
          this.$store.commit('SET_POWER_BDD_ON', x.data.power.bdd.on_state)
          this.$store.commit('SET_POWER_BDD_AIM_VOLTAGE', x.data.power.bdd.aim_voltage)
          this.$store.commit('SET_POWER_BE_ON', x.data.power.be.on_state)
          this.$store.commit('SET_POWER_BE_AIM_VOLTAGE', x.data.power.be.aim_voltage)
          this.$store.commit('SET_DEP_VOLTAGE', x.data.dep.voltage)
          this.$store.commit('SET_DEP_PERIOD', x.data.dep.period)
          this.$store.commit('SET_DEP_LOOP_STATE', x.data.dep.loop_state)
        })
        .catch(error => {
          console.log(error)
        })
    },
    connect () {
      this.isLoading = true
      axios.post('http://10.6.1.86:5000/api/power')
        .then((response) => {
          // console.log(response.data)
          this.isLoading = false
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  beforeCreate () {

  },
  mounted () {
    this.$store.dispatch('INIT_STATE').then(() => {
      this.data_done = true
      this.interval = setInterval(this.update_data, 200)
    })
  },
  beforeDestroy () {
    if (this.interval) {
      clearInterval(this.interval)
      this.interval = undefined
    }
  }
}
</script>

<style>

.load_btn{
  /* position: fixed; */
  /* top: 140; */
  border-radius: 10px;
  padding: 7px 20px;
  background-color: rgba(218, 149, 0, 0.822);
}
body {
  background-color: #121212;
  /* min-width:1250px;        */
}
/* .header-bg{
  position: absolute;
  top: 10px;
} */
/* .main{
  margin-top: 10px;
} */
.tabs{
  max-width: 1920px;
}
.div_top {
display: grid;
grid-template-columns: repeat(5, 1fr);
grid-template-rows: repeat(5, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
}

.div_btn { grid-area: 1 / 1 / 6 / 6; min-width: 600px;}
.div_tabs { grid-area: 1 / 1 / 2 / 2; position: absolute; margin-left: 35px;}
</style>
