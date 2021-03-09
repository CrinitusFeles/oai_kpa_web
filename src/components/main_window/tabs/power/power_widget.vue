<template>
    <div class="parent">
        <div class="div1"> {{ msg }} </div>
        <div class="div2"> 
          <div class="form_radio_btn">
            <input id="be_power_on" type="radio" name="be" value="1" v-on:change="button_click_handler($event)">
            <label for="be_power_on" id="label_power_on"> ВКЛ </label>
          </div>
        </div>
        <div class="div3"> 
          <div class="form_radio_btn">
            <input id="be_power_off" type="radio" name="be" value="2" v-on:change="button_click_handler($event)">
            <label for="be_power_off" id="label_power_off"> ОТКЛ </label>
          </div>
        </div>
        <div class="div4"> Напряжение </div>
        <div class="div5" id="be_voltage_val"> {{ voltage }} </div>
        <div class="div6"> Ток, мА: </div>
        <div class="div7" id="be_current_val"> {{ current }} </div>
        <div class="div8"> Мощность, мВт: </div>
        <div class="div9" id="be_power_val"> {{ power }} </div>
        <div class="div10"> <a class="btn_material" id="be_aim_voltage_btn" v-on:click="button_click_handler($event)"> Целевое напряжение, В </a> </div>
        <div class="div11"> <vue-number-input center controls v-model="value" style="color: black;"></vue-number-input>
        </div> 
    </div>
</template>
<script>
import VueNumberInput from '@chenfengyuan/vue-number-input'
import axios from 'axios'

export default {
  props: ['msg'],
  data: function () {
    return {
      voltage: 0.00,
      current: 0.00,
      power: 0.00,
      aim_voltage: 2.00,
      value: 0
    }
  },
  components: {
    VueNumberInput
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
    update_data (data) {
      if (data && data.voltage) {
        this.power_data = data
        this.voltage = data.voltage
        this.current = data.current
        this.power = data.power
        if (this.msg === 'БЭ') {
          if (this.voltage >= data.aim_voltage + 0.5 || this.voltage <= data.aim_voltage - 0.5) {
            document.getElementById('be_voltage_val').style.color = 'tomato'
          } else {
            document.getElementById('be_voltage_val').style.color = '#84C9FB'
          }
          if (this.current >= 15 || this.current <= 1) {
            document.getElementById('be_current_val').style.color = 'tomato'
          } else {
            document.getElementById('be_current_val').style.color = '#84C9FB'
          }
        } else {
          if (this.voltage >= data.aim_voltage + 0.5 || this.voltage <= data.aim_voltage - 0.5) {
            document.getElementById('power_bdd_voltage_val').style.color = 'tomato'
          } else {
            document.getElementById('power_bdd_voltage_val').style.color = '#84C9FB'
          }
          if (this.current >= 15 || this.current <= 1) {
            document.getElementById('power_bdd_current_val').style.color = 'tomato'
          } else {
            document.getElementById('power_bdd_current_val').style.color = '#84C9FB'
          }
        }
      }
    },
    button_click_handler (event) {
      if (event.target.id === 'be_power_on') {
        console.log('be_power_on ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'be_power_off') {
        console.log('be_power_off ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'be_aim_voltage_btn') {
        console.log('be_aim_voltage ' + this.value)
        this.sendData({button: event.target.id, state: this.value})
      } else if (event.target.id === 'power_bdd_on_id') {
        console.log('bdd_power_on ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'power_bdd_off_id') {
        console.log('bdd_power_off ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'power_bdd_aim_voltage_btn') {
        console.log('bdd_aim_voltage ' + this.value)
        this.sendData({button: event.target.id, state: this.value})
      }
    }
  },
  mounted () {
    // this.update_data()
    if (this.msg === 'БЭ') {
      this.value = this.$store.getters.GET_POWER_BDD_AIM_VOLTAGE
      document.getElementById('be_power_off').setAttribute('name', 'bdd')
      document.getElementById('be_power_on').setAttribute('name', 'bdd')
      document.getElementById('be_power_off').setAttribute('id', 'power_bdd_off_id')
      document.getElementById('be_power_on').setAttribute('id', 'power_bdd_on_id')
      document.getElementById('label_power_off').setAttribute('for', 'power_bdd_off_id')
      document.getElementById('label_power_on').setAttribute('for', 'power_bdd_on_id')
      document.getElementById('be_aim_voltage_btn').setAttribute('id', 'power_bdd_aim_voltage_btn')
      document.getElementById('be_voltage_val').setAttribute('id', 'power_bdd_voltage_val')
      document.getElementById('be_current_val').setAttribute('id', 'power_bdd_current_val')
      document.getElementById('be_power_val').setAttribute('id', 'power_bdd_power_val')

      document.getElementById('power_bdd_off_id').checked = !this.$store.getters.GET_POWER_BDD_ON
      document.getElementById('power_bdd_on_id').checked = this.$store.getters.GET_POWER_BDD_ON
      document.getElementById('be_power_off').checked = !this.$store.getters.GET_POWER_BE_ON
      document.getElementById('be_power_on').checked = this.$store.getters.GET_POWER_BE_ON
    } else {
      this.value = this.$store.getters.GET_POWER_BE_AIM_VOLTAGE
    }
  }
}
</script>

<style scoped>
.parent {
display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 0.5fr repeat(5, 1fr);
grid-column-gap: 4px;
grid-row-gap: 0px;

}

.div1 { grid-area: 1 / 1 / 2 / 3; }
.div2 { grid-area: 2 / 1 / 3 / 2; }
.div3 { grid-area: 2 / 2 / 3 / 3; }
.div4 { grid-area: 3 / 1 / 4 / 2; color: #84C9FB;}
.div5 { grid-area: 3 / 2 / 4 / 3; color: #84C9FB;}
.div6 { grid-area: 4 / 1 / 5 / 2; color: #84C9FB;}
.div7 { grid-area: 4 / 2 / 5 / 3; color: #84C9FB;}
.div8 { grid-area: 5 / 1 / 6 / 2; color: #84C9FB;}
.div9 { grid-area: 5 / 2 / 6 / 3; color: #84C9FB;}
.div10 { grid-area: 6 / 1 / 7 / 2; }
.div11 { grid-area: 6 / 2 / 7 / 3; }

</style>
