<template>
  <div class="container-fluid">
      <div class="row">
          <div class="col">
              <mku-widget/>
              <div class="power_widget">
                <power-top-widget ref="power_comp"/>
              </div>
          </div>
          <div class=col>
            <stm-table ref="stm_table_comp" v-bind:stm_apiData="this.stm_data"/>
            <dep-widget/>
          </div>
          <div class="col">
            <!-- <tests-widget/> -->
            <div class="chart_widget_panel">
              <div class="chart_widget">
              <chart ref="plotly_chart" align="center"/>
              </div>
              <div class="start_btn">
                <a class="btn_material" id="start_btn_id" v-on:click="chart_start_btn_click()"> Старт </a>
              </div>
              <div class="stop_btn">
                <a class="btn_material" id="stop_btn_id" v-on:click="chart_stop_btn_click()"> Стоп </a>
              </div>
              <div class="clear_btn">
                <a class="btn_material" id="clear_btn_id" v-on:click="chart_clear_btn_click()"> Очистить </a>
              </div>
            </div>
          </div>

      </div>
  </div>
</template>

<script>
import MyVuetable from './stm/MyVuetable'
import MkuWidget from './mku/mkuWidget'
import stmTable from './stm/stm_table'
import testsWidget from '../util_components/testsWidget.vue'
import PowerTopWidget from './power/power_top_widget'
import DepWidget from './dep/dep_widget'
// import Chart from '../util_components/Chart.vue'
import chart from '../util_components/plotly_chart.vue'
export default {
  data: function () {
    return {
      tabs_data: {
        stm: {},
        mpp: {},
        bdd: {}
      },
      update_bdk2: true,
      stm_data: {},
      data_done: false
    }
  },
  components: {
    chart, DepWidget, PowerTopWidget, MyVuetable, MkuWidget, stmTable, testsWidget
  },
  methods: {
    bdk2_tab_update_data (data) {
      if (data && data.stm) {
        this.stm_data = data
        if (this.update_bdk2) {
          this.$refs.stm_table_comp.update_data()
          this.$refs.power_comp.update_data(data.power)
        }
      }
    },
    chart_start_btn_click () {
      this.$refs.plotly_chart.start_update()
    },
    chart_stop_btn_click () {
      this.$refs.plotly_chart.stop_update()
    },
    chart_clear_btn_click () {
      this.$refs.plotly_chart.clear_data()
    }
  },
  mounted () {
    this.$emit('component-destroy', 'bdk2 tab mounted')
    this.$store.dispatch('INIT_STATE').then(() => {
      this.data_done = true
    })
    // this.interval = setInterval(this.update_data, 200)
  },
  beforeDestroy () {
    this.$emit('component-destroy', 'bdk2 tab destroyed')
    this.$refs.plotly_chart.stop_update()
  }
}
</script>

<style scoped>
.chart_widget_panel {
display: grid;
grid-template-columns: repeat(3, 1fr);
grid-template-rows: repeat(5, 1fr) 0.6fr;
grid-column-gap: 0px;
grid-row-gap: 0px;
background-color: #262833;
border-radius: 20px;
min-width: 560px;
}

.chart_widget { grid-area: 1 / 1 / 6 / 4; align-content: center;}
.start_btn { grid-area: 6 / 1 / 7 / 2; padding: 0px 15px;}
.stop_btn { grid-area: 6 / 2 / 7 / 3; padding: 0px 15px;}
.clear_btn { grid-area: 6 / 3 / 7 / 4; padding: 0px 15px;}


</style>