<template>
    <div class="container-fluid">
        <div class="col">
        <tabs :onSelect="onSelect">
            <tab title="БДК2" >
                <kpa-main-tab ref="bdk_tab" @component-destroy="destroy_handler"/>
            </tab>
            <tab id="stm_tab_id" :title=stm_status>
                This is React1
                <!-- <my-layout-composer></my-layout-composer> -->
            </tab>
            <tab id="be_tab_id" :title=be_status>
                <power-main-widget/>
            </tab>
            <tab id="bdd_tab_id" :title=bdd_status>
                <power-main-widget/>
            </tab>
            <tab id="mku_tab_id" :title=mku_status>
                <mku-main-widget/>
            </tab>
            <tab id="dep_tab_id" :title=dep_status>
                <dep-main-widget/>
            </tab>
            <tab id="interface_tab_id" :title=interface_status>

                <div class="terminal">
                  <shell 
                    :banner="banner"
                    :shell_input="send_to_terminal"
                    :commands="commands"
                    @shell_output="prompt"> 
                  </shell>
                </div>
                <div class="foreground">.</div>

            </tab>
        </tabs>
        </div>
    </div>
</template>

<script>
import kpaMainTab from './kpa_main_tab'
import { Tabs, Tab } from 'vue-slim-tabs'
import PowerMainWidget from './power/power_main_widget'
import MkuMainWidget from './mku/mku_main_widget'
import DepMainWidget from './dep/dep_main_widget'
import shell from './terminal'
export default {
  data: function () {
    return {
      stm_status: ['СТМ 🚫', false],
      be_status: ['Питание БЭ 🚫', false],
      bdd_status: ['Питание БДД 🚫', false],
      mku_status: ['МКУ 🚫', false],
      dep_status: ['ДЭП 🚫', false],
      interface_status: ['Интерфейс 🚫', false],
      active_tab: 0,
      send_to_terminal: '',
      tabs: document.getElementsByClassName('vue-tab'),
      commands: [
        {
          name: 'info',
          desc: 'Show information about this terminal',
          get () {
            return `<p style="color: white">With ❤️ By Salah Bentayeb @halasproject.</p>`
          }
        },
        {
          name: 'uname',
          desc: 'Show the current terminal name',
          get () {
            return `<p style="color: white">` + navigator.appVersion + `</p>`
          }
        }
      ],
      banner: {
        header: 'Командная строка БДК2',
        subHeader: 'Прием и передача modbus команд для КПА',
        helpHeader: 'Введите "help" для получения списка команд.',
        emoji: {
          first: '☠️',
          second: '💀',
          time: 750
        },
        sign: 'KPA $',
        img: {
          align: 'left',
          // link: '@/../../assets/logo.png',
          width: 175,
          height: 210
        }
      }
    }
  },
  components: {
    shell, kpaMainTab, Tabs, Tab, PowerMainWidget, MkuMainWidget, DepMainWidget
  },
  methods: {
    prompt (value) {
      if (value.trim() === 'ifconfig') {
        this.send_to_terminal = `
    Wi-Fi wireless network card:
        
    Local link IPv6 address. . . : fe80 :: 340f: 6f02: 41e9: 477b% 24
    IPv4 address. . . . . . . . .: 192.168.1.2
    Subnet mask. . . . . . . . . : 255.255.255.0
    Default Gateway. . . . . . . : 192.168.1.1`
      } else {
        this.send_to_terminal = `'${value}' is not recognized as an internal command or external,
an executable program or a batch file`
      }
    },
    update_tabs (data) {
      if (this.active_tab === 0) {
        this.$refs.bdk_tab.bdk2_tab_update_data(data)
      } else if (this.active_tab === 1) {
        this.$refs.stm_tab.stm_tab_update_data(data)
      }
      if (data.stm.connection_status === true) {
        this.stm_status = ['СТМ 🔌', true]
        this.tabs[1].style.background = '#2fb89d'
      } else {
        this.stm_status = ['СТМ 🚫', false]
        this.tabs[1].style.background = '#262833'
      }
      if (data.power.be.connection_status === true) {
        this.be_status = ['Питание БЭ 🔌', true]
        this.tabs[2].style.background = '#2fb89d'
      } else {
        this.be_status = ['Питание БЭ 🚫', false]
        this.tabs[2].style.background = '#262833'
      }
      if (data.power.bdd.connection_status === true) {
        this.bdd_status = ['Питание БДД 🔌', true]
        this.tabs[3].style.background = '#2fb89d'
      } else {
        this.bdd_status = ['Питание БДД 🚫', false]
        this.tabs[3].style.background = '#262833'
      }
      if (data.mku.connection_status === true) {
        this.mku_status = ['МКУ 🔌', true]
        this.tabs[4].style.background = '#2fb89d'
      } else {
        this.mku_status = ['МКУ 🚫', false]
        this.tabs[4].style.background = '#262833'
      }
      if (data.dep.connection_status === true) {
        this.dep_status = ['ДЭП 🔌', true]
        this.tabs[5].style.background = '#2fb89d'
      } else {
        this.dep_status = ['ДЭП 🚫', false]
        this.tabs[5].style.background = '#262833'
      }
      if (data.interface.connection_status === true) {
        this.interface_status = ['Интерфейс 🔌', true]
        this.tabs[6].style.background = '#2fb89d'
      } else {
        this.interface_status = ['Интерфейс 🚫', false]
        this.tabs[6].style.background = '#262833'
      }
    },
    onSelect (e, index) {
      this.active_tab = index
    },
    destroy_handler (value) {
      console.log(value)
      if (value === 'bdk2 tab mounted') {
        if (this.$parent.interval === undefined) {
          this.$parent.interval = setInterval(this.$parent.update_data, 200)
        }
      } else if (value === 'bdk2 tab destroyed') {
        clearInterval(this.$parent.interval)
        this.$parent.interval = undefined
      }
    }
  }
}
</script>

<!-- optionally use our default style -->
<style >

.foreground{
  top: 50px;
  height: 1300px;
  z-index: -1;
  background-image: url("../../../assets/img-noise-1200x900.png");
  top: 40px;
  position: absolute;
  width: 100%;
  
}
.terminal{
  height: 1300px;
  min-width: 1200px;
}
.col{
    max-height: 1000px;
}

.main_content{
    align-items: center;
    border: groove;
    
}
.vue-tablist {
  list-style: none;
  display: flex;
  padding-left: 0;
  border-bottom: 1px solid #e2e2e2;
  margin-left: 230px;
  z-index: 10;
}

.vue-tab {
  padding: 5px 10px;
  cursor: pointer;
  user-select: none;
  border: 1px solid transparent;
  border-bottom-color: #e2e2e2;
  border-radius: 3px 3px 0 0;
  background: #262833;
  color: rgb(206, 206, 206);
  position: relative;
  bottom: -1px;
  min-width: 155px;
  margin-left: 1px;
}

.vue-tab[aria-selected="true"] {
  background: rgba(0, 87, 218, 0.377);
  border-bottom-color: transparent;
  border: 4px solid rgba(0, 87, 218, 0.377);
}

.vue-tab[aria-disabled="true"] {
  cursor: not-allowed;
  color: #999;
}

</style>


