
<template>
    <div  v-if="data_done" class="page_background">
      <!-- <div class="header-bg"> 🚫🔌-->
        <!-- <connect-bar ref="connection_bar_comp"/> -->
      <!-- </div> -->
      <div class="div_top">
        <div class="div_content"> 
          <!-- <tabs class="tabs" ref="tabs_comp"> </tabs> -->
          
            <kpa-main-tab ref="bdk_tab" @component-destroy="destroy_handler"/>
            <shell/>
          
        </div>
        <div class="div_top_header"> 
          <!-- <div class="image"></div> -->
          <div class="header_background"></div>
          <div class="header_content">
              <div v-if="this.$vssWidth >= 800" class="logo" style="width: 230px; max-height: 120px;display: flex;align-items: center;justify-content: center;"> 
                <img class="image" src="../../assets/header_logo-bg.png" :width="'90%'" :height="'70%'"/> 
              </div>
              <div v-if="this.$vssWidth >= 1520" class="header_title"> Панель управления БДК2</div>
              <div class="row" id="header_connect_box" style="margin-left: 15px; display: flex; flex-wrap: nowrap;vertical-align: baseline;">
                <div class="connect_btn">  
                  <VueLoadingButton 
                  name="kek" 
                  class="load_btn" 
                  @click.native="connect" 
                  :loading="isLoading" 
                  :styled="false"
                  style="margin-right: 15px; padding: 15px 15px; color: #222222;"> 
                  
                  Подключиться 
                  </VueLoadingButton>
                </div>
                <div class="devices_list">
                  <VueFaqAccordion 
                    id="accordion"
                    :items="myItems"
                    :activeColor="'#0f0'"
                    :fontColor="'#d8d8d8'"
                    :borderColor="'none'"
                    style="width: 480px; border-radius: 20px; background-color: #262833D1; margin-right: 40px; font-size: 18px; font-family: glasten;"
                  />
              </div>
            </div>
          </div>
            
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import tabs from './tabs/tabs'
import ConnectBar from './connect_bar'
import VueLoadingButton from 'vue-loading-button'
import kpaMainTab from './tabs/kpa_main_tab'
import VueFaqAccordion from 'vue-faq-accordion'
import VueScreenSize from 'vue-screen-size'
import shell from './tabs/terminal_kpa'
export default {
  data () {
    return {
      isLoading: false,
      interval: undefined,
      model_data: {},
      data_done: false,
      stm_status: 'СТМ: Не подключен 🚫',
      be_status: 'Питание БЭ: Не подключен 🚫',
      bdd_status: 'Питание БДД: Не подключен 🚫',
      mku_status: 'МКУ: Не подключен 🚫',
      mko_status: 'МКО: Не подключен 🚫',
      dep_status: 'ДЭП: Не подключен 🚫',
      interface_status: 'Интерфейс: Не подключен 🚫',
      calculated_margin: this.$vssWidth > 800 ? 0 : 100

    }
  },
  computed: {
    myItems () {
      return [{
        title: 'Статус подключения устройств',
        value: '<div class="list_element"> ' + this.be_status + ' </div> <div class="list_element">' + this.bdd_status + '</div> <div class="list_element">' + this.stm_status + '</div> <div class="list_element">' + this.mku_status + '</div> <div class="list_element">' + this.mko_status + '</div> <div class="list_element">' + this.dep_status + '</div> <div class="list_element">' + this.interface_status + '</div>'
      }]
    }
  },
  mixins: [VueScreenSize.VueScreenSizeMixin],
  components: { shell, VueFaqAccordion, kpaMainTab, tabs, ConnectBar, VueLoadingButton },
  methods: {
    update_data () {
      axios.get('http://10.6.1.86:5000/api/view_model')
        .then(x => {
          // this.$refs.tabs_comp.update_tabs(x.data)
          this.$refs.bdk_tab.bdk2_tab_update_data(x.data)
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
          // console.log(typeof(this.myItems()))
          if (x.data.stm.connection_status === true) {
            this.stm_status = 'СТМ: ОК 🔌'
          } else {
            this.stm_status = 'СТМ: Не подключен 🚫'
          }
          if (x.data.power.be.connection_status === true) {
            this.be_status = 'Питание БЭ: ОК 🔌'
          } else {
            this.be_status = 'Питание БЭ: Не подключен 🚫'
          }
          if (x.data.power.bdd.connection_status === true) {
            this.bdd_status = 'Питание БДД: ОК 🔌'
          } else {
            this.bdd_status = 'Питание БДД: Не подключен 🚫'
          }
          if (x.data.mku.connection_status === true) {
            this.mku_status = 'МКУ: ОК 🔌'
          } else {
            this.mku_status = 'МКУ: Не подключен 🚫'
          }
          if (x.data.dep.connection_status === true) {
            this.dep_status = 'ДЭП: ОК 🔌'
          } else {
            this.dep_status = 'ДЭП: Не подключен 🚫'
          }
          if (x.data.interface.connection_status === true) {
            this.interface_status = 'Интерфейс: ОК 🔌'
          } else {
            this.interface_status = 'Интерфейс: Не подключен 🚫'
          }
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
    },
    destroy_handler (value) {
      console.log(value)
      if (value === 'bdk2 tab mounted') {
        if (this.interval === undefined) {
          this.interval = setInterval(this.update_data, 200)
        }
      } else if (value === 'bdk2 tab destroyed') {
        clearInterval(this.interval)
        this.interval = undefined
      }
    }
  },

  beforeCreate () {

  },
  mounted () {
    this.$store.dispatch('INIT_STATE').then(() => {
      this.data_done = true
      this.interval = setInterval(this.update_data, 200)
    })
    console.log(document.getElementsByClassName('accordion__title'))
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
@font-face {
    font-family: "glasten";
    src: url("../../assets/Stamper-RG/7fonts.ru_Stamper_RG.ttf");
}
.load_btn{
  /* position: fixed; */
  /* top: 140; */
  border-radius: 10px;
  padding: 7px 20px;
  background-color: rgba(218, 149, 0, 0.822);
}
.load_btn:disabled {
  pointer-events: stroke;
  cursor: not-allowed;
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
.list_element:hover{
  color: red;
}

.div_top {
display: grid;
grid-template-columns: repeat(5, 1fr);
grid-template-rows: repeat(5, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
}

.div_content { 
  grid-area: 1 / 1 / 6 / 6;
  min-width: 600px; 
  margin-top: 130px; 
  margin-left: 60px; 
  margin-right: 60px;
  display: flex;
  align-items: center; /* Vertical center alignment */
  justify-content: center; /* Horizontal center alignment */
  flex-wrap: wrap;
}


.div_top_header {
display: grid;
grid-template-columns: 1fr;
grid-template-rows: 1fr;
grid-column-gap: 0px;
grid-row-gap: 0px;
position: absolute;
z-index: 100;
align-content: right;
width: 100%;
}

.image {  grid-area: 1 / 1 / 2 / 2; margin-top: 5px; margin-left: 60px;}
.header_title { 
  grid-area: 1 / 1 / 2 / 2;
  color: #84c9fbd5; 
  font-family: glasten;
  /* font-weight: bold; */
  z-index: 10; 
  display: flex;
  align-items: center; /* Vertical center alignment */
  justify-content: center; /* Horizontal center alignment */
  font-size: 40px;
  min-width: 400px;
}
.header_content{
  grid-area: 1 / 1 / 2 / 2;
  display: flex;
  align-items: right;
  justify-content: space-between;
  flex-direction: row;
  width: 100%;
}
.connect_btn {  
    font-family: glasten;
  display: flex;
  align-items: center; /* Vertical center alignment */
  justify-content: center; /* Horizontal center alignment */ }
.devices_list { grid-area: 1 / 4 / 2 / 5; max-height: 40px;}
.header_background { grid-area: 1 / 1 / 2 / 5; background-color: #0030538e; height: 120px; width: 100%;}
</style>
