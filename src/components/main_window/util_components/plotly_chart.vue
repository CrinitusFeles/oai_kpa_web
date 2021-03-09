<template>
  <div id="my_chart">
    <!-- <Plotly v-bind:data="data" v-bind:layout="layout" :display-mode-bar="true"></Plotly> -->
  </div>
</template>

<script>
// import {Plotly} from 'vue-plotly'
// import myPlotly from '../../../'
import Plotly from 'plotly.js-dist'
export default {
  components: {

  },
  data: function () {
    return {
      points_count: 0,
      val: 0,
      interval: undefined,
      data: [{
        x: [],
        y: [],
        name: 'Напряжение БЕ',
        type: 'scatter'
      },
      {
        x: [],
        y: [],
        name: 'Ток БЕ',
        yaxis: 'y2',
        type: 'scatter'
      },
      {
        x: [],
        y: [],
        name: 'Напряжение БДД',
        type: 'scatter'
      },
      {
        x: [],
        y: [],
        name: 'Ток БДД',
        yaxis: 'y2',
        type: 'scatter'
      }],
      layout: {
        title: 'Мониторинг питания БЕ и БДД',
        titlefont: {color: 'orange'},
        legend: {
          x: 0.3,
          // xanchor: 'right',
          y: 1.15,
          orientation: 'h',
          font: {
            family: 'sans-serif',
            size: 12,
            color: '#d8d8d8'
          }
        },
        xaxis: {
          range: [0, 39],
          titlefont: {color: 'orange'},
          tickfont: {color: 'orange'}
        },
        yaxis: {
          title: 'Напряжение, В',
          range: [-2, 2],
          titlefont: {color: 'orange'},
          tickfont: {color: 'orange'}
        },
        yaxis2: {
          range: [-2, 2],
          title: 'Ток, мА',
          titlefont: {color: 'orange'},
          tickfont: {color: 'orange'},
          overlaying: 'y',
          side: 'right'
        },
        plot_bgcolor: 'rgba(0, 0, 0, 0.5)',
        paper_bgcolor: 'rgba(0, 0, 0, 0)'
      },
      config: {responsive: true}
    }
  },
  mounted () {
    Plotly.newPlot('my_chart', this.data, this.layout, this.config)
  },
  methods: {
    update_chart () {
      var data = new Date()
      this.val += 0.1
      this.data[0].y.push(Math.sin(this.val * 2 * Math.PI))
      this.data[0].x.push(data.toLocaleString('ru', { hour: '2-digit', minute: '2-digit', second: '2-digit' }))
      this.data[1].y.push(Math.random() + 10)
      this.data[1].x.push(data.toLocaleString('ru', { hour: '2-digit', minute: '2-digit', second: '2-digit' }))
      this.data[2].y.push(Math.cos(this.val * 2 * Math.PI))
      this.data[2].x.push(data.toLocaleString('ru', { hour: '2-digit', minute: '2-digit', second: '2-digit' }))
      this.data[3].y.push(Math.random() + 10)
      this.data[3].x.push(data.toLocaleString('ru', { hour: '2-digit', minute: '2-digit', second: '2-digit' }))

      this.points_count += 1
      if (this.points_count === 40) {
        this.data[0].y.shift()
        this.data[0].x.shift()
        this.data[1].y.shift()
        this.data[1].x.shift()
        this.data[2].y.shift()
        this.data[2].x.shift()
        this.data[3].y.shift()
        this.data[3].x.shift()
        this.points_count -= 1
      }
      Plotly.animate('my_chart', {
        data: this.data,
        traces: [0, 1, 2, 3],
        layout: {}
      }, {
        transition: {
          duration: 0,
          easing: 'cubic-in-out'
        },
        frame: {
          duration: 500
        }
      })
    },
    getData () {
      return Math.random()
    },
    stop_update () {
      clearInterval(this.interval)
      console.log('stop')
    },
    start_update () {
      this.interval = setInterval(this.update_chart, 1000)
      console.log('start')
    },
    clear_data () {
      this.data[0].y = []
      this.data[0].x = []
      this.data[1].y = []
      this.data[1].x = []
      this.data[2].y = []
      this.data[2].x = []
      this.data[3].y = []
      this.data[3].x = []
      this.points_count = 0
      Plotly.animate('my_chart', {
        data: this.data,
        traces: [0, 1, 2, 3],
        layout: {}
      }, {
        transition: {
          duration: 0,
          easing: 'cubic-in-out'
        },
        frame: {
          duration: 300
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
