<template>
    <div class="parent"> 
        <div class="div1"> МКУ </div>
        <div class="div2"> БЭ </div>
        <div class="div3"> БДД </div>
        <div class="div4"> 
          <div class="form_radio_btn">
            <input id="pk1_radiobtn" type="radio" name="mku_bdd_group3" value="1" v-on:change="button_click_handler($event)">
            <label for="pk1_radiobtn"> ПК1 </label>
          </div>
        </div>
        <div class="div5"> 
          <div class="form_radio_btn">
            <input id="pk2_radiobtn" type="radio" name="mku_bdd_group3" value="2" v-on:change="button_click_handler($event)">
            <label for="pk2_radiobtn"> ПК2 </label>
          </div>
        </div>
        <div class="div6"> 
          <div class="form_radio_btn">
            <input id="bdd_on" type="radio" name="mku_bdd_group1" value="1" v-on:change="button_click_handler($event)">
            <label for="bdd_on"> БДД ВКЛ </label>
          </div>
        </div>
        <div class="div7"> 
          <div class="form_radio_btn">
            <input id="tk_on" type="radio" name="mku_bdd_group2" value="1" v-on:change="button_click_handler($event)">
            <label for="tk_on"> ТК ВКЛ </label>
          </div>
        </div>
        <div class="div8"> 
            <a class="btn_material" v-on:click="mku_off_click"> ОТКЛ </a>
        </div>
        <div class="div9"> 
          <div class="form_radio_btn">
            <input id="bdd_off" type="radio" name="mku_bdd_group1" value="2" v-on:change="button_click_handler($event)">
            <label for="bdd_off"> БДД ОТКЛ </label>
          </div>
        </div>
        <div class="div10"> 
          <div class="form_radio_btn">
            <input id="tk_off" type="radio" name="mku_bdd_group2" value="2" v-on:change="button_click_handler($event)">
            <label for="tk_off"> ТК ОТКЛ </label>
          </div>
        </div>
        <div class="div11"> 
          <a class="btn_material" id="mku_set_duration_btn" v-on:click="button_click_handler($event)"> Длительность импульса, мс </a> 
        </div>
        <div class="div12"> <vue-number-input id="imp_duration" center controls v-model="value" style="color: black;"></vue-number-input> </div>
    </div>
</template>

<script>
import VueNumberInput from '@chenfengyuan/vue-number-input'
import axios from 'axios'

export default {
  components: {
    VueNumberInput
  },
  methods: {
    sendData (arg1) {
      axios.post('http://192.168.31.9:5000/api/button_handler', arg1)
        .then((response) => {
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    mku_off_click () {
      document.getElementById('pk1_radiobtn').checked = false
      document.getElementById('pk2_radiobtn').checked = false
      console.log('all pk off')
      this.sendData({button: 'mku_off_btn', state: true})
    },
    button_click_handler (event) {
      if (event.target.id === 'pk1_radiobtn') {
        console.log('pk1 ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'pk2_radiobtn') {
        console.log('pk2 ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'bdd_on') {
        console.log('bdd_on ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'bdd_off') {
        console.log('bdd_off ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'tk_on') {
        console.log('tk_on ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'tk_off') {
        console.log('tk_off ' + event.target.checked)
        this.sendData({button: event.target.id, state: event.target.checked})
      } else if (event.target.id === 'mku_set_duration_btn') {
        console.log(this.value)
        this.sendData({button: event.target.id, state: this.value})
      }
    }
  },
  data: function () {
    return {
      value: 0
    }
  },
  mounted () {
    document.getElementById('pk1_radiobtn').checked = this.$store.getters.GET_MKU_PK1
    document.getElementById('pk2_radiobtn').checked = this.$store.getters.GET_MKU_PK2
    document.getElementById('bdd_on').checked = this.$store.getters.GET_MKU_BDD_ON
    document.getElementById('bdd_off').checked = !this.$store.getters.GET_MKU_BDD_ON
    document.getElementById('tk_on').checked = this.$store.getters.GET_MKU_TK_ON
    document.getElementById('tk_off').checked = !this.$store.getters.GET_MKU_TK_ON
    this.value = this.$store.getters.GET_MKU_DURATION
  }
}
</script>

<style scoped>
@import '../../../../assets/radioButton.css';

.parent {
display: grid;
grid-template-columns: repeat(4, 1fr);
grid-template-rows: repeat(2, 0.5fr) repeat(3, 1fr);
grid-column-gap: 4px;
grid-row-gap: 0px;
min-width: 560px;
background-color: #262833;
border-radius: 20px;
color: #d8d8d8;;
margin-bottom: 10px;
padding: 10px 15px;
}

.div1 { 
  grid-area: 1 / 1 / 2 / 5; 
  background: rgba(0, 87, 218, 0.377);
  color: #d8d8d8;
  border-radius: 7px;
  font-weight: bold;
  color: #84C9FB;
}
.div2 { grid-area: 2 / 1 / 3 / 3; }
.div3 { grid-area: 2 / 3 / 3 / 5; }
.div4 { grid-area: 3 / 1 / 4 / 2; }
.div5 { grid-area: 3 / 2 / 4 / 3; }
.div6 { grid-area: 3 / 3 / 4 / 4; }
.div7 { grid-area: 3 / 4 / 4 / 5; }
.div8 { grid-area: 4 / 1 / 5 / 3; }
.div9 { grid-area: 4 / 3 / 5 / 4; }
.div10 { grid-area: 4 / 4 / 5 / 5; }
.div11 { grid-area: 5 / 1 / 6 / 3; }
.div12 { grid-area: 5 / 3 / 6 / 5; }
</style>