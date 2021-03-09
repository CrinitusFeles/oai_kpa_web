<template>
    <div class="parent">
        <div class="div1"> Питание </div>
        <div class="div2"> <power-widget msg="БДД" ref="power_bdd_comp"/> </div>
        <div class="div3"> <power-widget msg="БЭ" ref="power_be_comp"/> </div>
    </div>
</template>

<script>
import PowerWidget from './power_widget.vue'
export default {
  data: function () {
    return {
      power_data: {
        bdd: {},
        be: {}
      }
    }
  },
  components: {
    PowerWidget
  },
  methods: {
    update_data (data) {
      this.power_data = data
      this.$refs.power_bdd_comp.update_data(data.bdd, data.bdd.on_state, data.be.on_state)
      this.$refs.power_be_comp.update_data(data.be, data.bdd.on_state, data.be.on_state)
    }
  },
  mounted () {
  }
}
</script>

<style scoped>
.parent {
display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 0.5fr repeat(10, 1fr);
grid-column-gap: 4px;
grid-row-gap: 0px;
background-color: #262833;
border-radius: 20px;
color: white;
margin-bottom: 10px;
padding: 10px 15px;
/* min-width: 560px; */
}

.div1 { 
  grid-area: 1 / 1 / 2 / 3; 
  background: rgba(0, 87, 218, 0.377);
  color: white;
  border-radius: 7px;
  font-weight: bold;
  color: #84C9FB;
}
.div2 { grid-area: 2 / 1 / 7 / 3; color: #d8d8d8;}
.div3 { grid-area: 7 / 1 / 12 / 3; color: #d8d8d8;}
</style>