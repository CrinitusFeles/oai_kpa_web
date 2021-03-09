<template>
    <div class="parent">
        <div class="div1" id="stm"> Подключение СТМ: {{stm_status}} </div>
        <div class="div2" id="mku"> Подключение МКУ: {{mku_status}} </div>
        <div class="div3" id="bdd"> Подключение БДД: {{bdd_status}}</div>
        <div class="div4" id="be"> Подключение БЭ: {{be_status}}</div>
        <div class="div5" id="dep"> Подключение ДЭП: {{dep_status}}</div>
        <div class="div6" id="interface"> Подключение Интерфейс: {{interface_status}}</div>
        <div class="div7"> <VueLoadingButton @click.native="connect" aria-label="Send message" :styled="true" :loading="isLoading"/> </div>
    </div>
</template>
<script>
import VueLoadingButton from 'vue-loading-button'
import axios from 'axios'

export default {
  data () {
    return {
      stm_status: 'отсутствует',
      mku_status: 'отсутствует',
      bdd_status: 'отсутствует',
      be_status: 'отсутствует',
      dep_status: 'отсутствует',
      interface_status: 'отсутствует',
      isLoading: false,
      isStyled: false,
      connected_color: 'green',
      disconnected_color: '#fcdab7'
    }
  },
  components: {
    VueLoadingButton
  },
  methods: {
    connect () {
      this.isLoading = true
      axios.post('http://192.168.31.9:5000/api/power')
        .then((response) => {
          // console.log(response.data)
          this.isLoading = false
        })
        .catch(error => {
          console.log(error)
        })
    },
    update_status (data) {
      if (data.stm.connection_status === true) {
        this.stm_status = 'OK'
        document.getElementById('stm').style.background = this.connected_color
      } else {
        this.stm_status = 'Отсутствует'
        document.getElementById('stm').style.background = this.disconnected_color
      }
      if (data.mku.connection_status === true) {
        this.mku_status = 'OK'
        document.getElementById('mku').style.background = this.connected_color
      } else {
        this.mku_status = 'Отсутствует'
        document.getElementById('mku').style.background = this.disconnected_color
      }
      if (data.power.bdd.connection_status === true) {
        this.bdd_status = 'OK'
        document.getElementById('bdd').style.background = this.connected_color
      } else {
        this.bdd_status = 'Отсутствует'
        document.getElementById('bdd').style.background = this.disconnected_color
      }
      if (data.power.be.connection_status === true) {
        this.be_status = 'OK'
        document.getElementById('be').style.background = this.connected_color
      } else {
        this.be_status = 'Отсутствует'
        document.getElementById('be').style.background = this.disconnected_color
      }
      if (data.dep.connection_status === true) {
        this.dep_status = 'OK'
        document.getElementById('dep').style.background = this.connected_color
      } else {
        this.dep_status = 'Отсутствует'
        document.getElementById('dep').style.background = this.disconnected_color
      }
      if (data.interface.connection_status === true) {
        this.interface_status = 'OK'
        document.getElementById('interface').style.background = this.connected_color
      } else {
        this.interface_status = 'Отсутствует'
        document.getElementById('interface').style.background = this.disconnected_color
      }
    }
  }
}
</script>
<style scoped>
.parent {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 4px;
    grid-row-gap: 0px;
    border: groove;
    margin-bottom: 50px;
}

.div1 { grid-area: 1 / 1 / 2 / 2; background: #CF6679;}
.div2 { grid-area: 1 / 2 / 2 / 3; background: #CF6679;}
.div3 { grid-area: 1 / 3 / 2 / 4; background: #CF6679;}
.div4 { grid-area: 1 / 4 / 2 / 5; background: #CF6679;}
.div5 { grid-area: 1 / 5 / 2 / 6; background: #CF6679;}
.div6 { grid-area: 1 / 6 / 2 / 7; background: #CF6679;}
.div7 { grid-area: 1 / 7 / 2 / 8; }
</style>