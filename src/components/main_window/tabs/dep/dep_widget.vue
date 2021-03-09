<template>
    <div class="parent">
        <div class="div1"> ДЭП </div>
        <div class="div2"> Напряжение ДЭП </div>
        <div class="div3"> 
          <div class="form_radio_btn">
            <input id="dep_pos_voltage" type="radio" name="dep_voltage" value="1" v-on:change="button_click_handler($event)">
            <label for="dep_pos_voltage"> 30 B </label>
          </div>
        </div>
        <div class="div4"> 
          <div class="form_radio_btn">
            <input id="dep_zero_voltage" type="radio" name="dep_voltage" value="2" v-on:change="button_click_handler($event)">
            <label for="dep_zero_voltage"> 0 B </label>
          </div>
        </div>
        <div class="div5">
          <div class="form_radio_btn">
            <input id="dep_neg_voltage" type="radio" name="dep_voltage" value="3" v-on:change="button_click_handler($event)">
            <label for="dep_neg_voltage"> -30 B </label>
          </div>
        </div>
        <div class="div6"> Циклическое воздействие</div>
        <div class="div7"> 
          <a class="btn_material" id="aim_voltage_btn" v-on:click="button_click_handler($event)"> Период, с </a> 
        </div>
        <div class="div8"> <vue-number-input center controls v-model="value" style="color: black;"></vue-number-input>
        </div>
        <div class="div9"> 
          <div class="form_radio_btn">
            <input id="dep_loop_start" type="radio" name="dep_loop" value="1" v-on:change="button_click_handler($event)" >
            <label for="dep_loop_start"> Старт </label>
          </div>
        </div>
        <div class="div10"> 
          <div class="form_radio_btn">
            <input id="dep_loop_stop" type="radio" name="dep_loop" value="2" v-on:change="button_click_handler($event)">
            <label for="dep_loop_stop"> Стоп </label>
          </div>
        </div>
    </div>
</template>

<script>
import VueNumberInput from '@chenfengyuan/vue-number-input'
import axios from 'axios'

export default {
  data: function () {
    return {
      value: 0
    }
  },
  methods: {
    sendData (arg1) {
      axios.post('http://10.6.1.86:5000/api/button_handler', arg1)
        .then((response) => {
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    button_click_handler (event) {
      if (event.target.id === 'dep_pos_voltage') {
        console.log('dep_pos_voltage ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'dep_zero_voltage') {
        console.log('dep_zero_voltage ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'dep_neg_voltage') {
        console.log('dep_neg_voltage ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'dep_loop_start') {
        console.log('dep_loop_start ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'dep_loop_stop') {
        console.log('dep_loop_stop ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'aim_voltage_btn') {
        console.log(this.value)
        this.sendData({button: event.target.id, state: this.value})
      } else if (event.target.id === 'dep_loop_start') {
        console.log('dep_loop_start ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'dep_loop_stop') {
        console.log('dep_loop_stop ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      }
    }
  },
  components: {
    VueNumberInput
  },
  mounted () {
    if (this.$store.getters.GET_DEP_VOLTAGE === 30) {
      document.getElementById('dep_pos_voltage').checked = true
    } else if (this.$store.getters.GET_DEP_VOLTAGE === 0) {
      document.getElementById('dep_zero_voltage').checked = true
    } else if (this.$store.getters.GET_DEP_VOLTAGE === -30) {
      document.getElementById('dep_neg_voltage').checked = true
    } else {
      alert('Warning! dep module recieve incorrect voltage != [0, 30, -30]')
    }
    document.getElementById('dep_loop_start').checked = this.$store.getters.GET_DEP_LOOP_STATE
    document.getElementById('dep_loop_stop').checked = !this.$store.getters.GET_DEP_LOOP_STATE
    this.value = this.$store.getters.GET_DEP_PERIOD
  }
}
</script>

<style scoped>
/* @import '../assets/radioButton.css'; */
.parent {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(2, 0.5fr) 1fr 0.5fr repeat(2, 1fr);
    grid-column-gap: 4px;
    grid-row-gap: 0px;

    background-color: #262833;
    border-radius: 20px;
    color: white;
    margin-bottom: 10px;
    padding: 10px 15px;
    min-width: 560px;
}

.div1 { 
  grid-area: 1 / 1 / 2 / 7; 
  background: rgba(0, 87, 218, 0.377);
  color: white;
  border-radius: 7px;
  font-weight: bold;
  color: #84C9FB;
}
.div2 { grid-area: 2 / 1 / 3 / 7; color: #d8d8d8}
.div3 { grid-area: 3 / 1 / 4 / 3; }
.div4 { grid-area: 3 / 3 / 4 / 5; }
.div5 { grid-area: 3 / 5 / 4 / 7; }
.div6 { grid-area: 4 / 1 / 5 / 7; color: #d8d8d8}
.div7 { grid-area: 5 / 1 / 6 / 4; }
.div8 { grid-area: 5 / 4 / 6 / 7; }
.div9 { grid-area: 6 / 1 / 7 / 4; }
.div10 { grid-area: 6 / 4 / 7 / 7; }

</style>