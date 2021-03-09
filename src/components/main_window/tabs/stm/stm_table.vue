<template>
    <div class="parent">
        <div class="div1"> СТМ </div>
        <div class="div2"> 
          <my-vuetable ref="child_table1" v-bind:myapiData="this.apiData.stm.table1"></my-vuetable> 
          <div class="KS" style="margin-top: 253px;" > Контроль стыковки </div>
          <my-vuetable ref="child_table4" v-bind:myapiData="this.apiData.stm.table4"></my-vuetable>
        </div>
        <div class="div3"> <my-vuetable ref="child_table2" v-bind:myapiData="this.apiData.stm.table2"></my-vuetable> </div>
        <div class="div4"> <my-vuetable ref="child_table3" v-bind:myapiData="this.apiData.stm.table3"></my-vuetable> </div>
    </div>
</template>

<script>
import MyVuetable from './MyVuetable'
// import { Row, Column } from 'vue-grid-responsive'
export default {
  props: ['stm_apiData'],
  data: function () {
    return {
      apiData: {
        stm: {
          table1: {},
          table2: {},
          table3: {},
          table4: {}
        }
      }
    }
  },
  components: {
    MyVuetable
  },
  mounted () {
    this.$store.dispatch('INIT_STATE')
    // setInterval(this.update_data, 2000)
  },
  methods: {
    update_data () {
      if (this.stm_apiData && this.stm_apiData.stm) {
        this.apiData = this.stm_apiData
        // console.log(this.apiData)
        this.$refs.child_table1.print_data()
        this.$refs.child_table2.print_data()
        this.$refs.child_table3.print_data()
        this.$refs.child_table4.print_data()
      }
    }
  }
}
</script>

<style scoped>
/* .col{
    background: rgb(54, 134, 255);
    color: white;
    border-radius: 7px;
    font-weight: bold;
} */

.parent {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: 0.2fr repeat(4, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 0px;

    margin-right: 15px;
    min-width: 560px;
    width: 100%;
    background-color: #262833;
    border-radius: 20px;
    margin-bottom: 10px;
    padding: 10px 15px;
}

.div1 { grid-area: 1 / 1 / 2 / 4; 
  background: rgba(0, 87, 218, 0.377);
  color: #84C9FB;
  border-radius: 7px;
  font-weight: bold;}
.div2 { grid-area: 2 / 1 / 6 / 2; }
.div3 { grid-area: 2 / 2 / 6 / 3; }
.div4 { grid-area: 2 / 3 / 6 / 4; }
.KS{
  background: rgba(0, 87, 218, 0.377);
  color: #84C9FB;
  border-radius: 7px;
  font-weight: bold;
  padding: 5px 5px;
}
</style>