<template>
  <vuetable ref="vuetable"
    :api-mode="false"
    :data="apiData"
    :fields="fields"
    pagination-path=""
  ></vuetable>
</template>

<script>
import Vuetable from 'vuetable-2/src/components/Vuetable'
import $http from 'axios'
export default {
  components: {
    Vuetable
  },
  props: ['model', 'myapiData'],
  data: function () {
    return {
      apiData: undefined,
      stateColor1: '#2fb89d',
      stateColor2: 'orange',
      stateColor3: 'tomato',
      fields: [
        {
          name: 'label',
          title: ''
        },
        {
          name: 'id',
          title: '',
          callback: 'checkState'
        }
      ]
    }
  },
  methods: {
    checkState (value) {
      if (this.myapiData) {
        if (this.myapiData.data[value].state === 0) {
          return '<div style="background-color: ' + this.stateColor1 + '; border-radius: 10px; padding: 5px 5px; font-weight: bold;">' + this.myapiData.data[value].value
        } else if (this.apiData.data[value].state === 1) {
          return '<div style="background-color: ' + this.stateColor2 + '; border-radius: 10px; padding: 5px 5px; font-weight: bold;">' + this.myapiData.data[value].value
        } else if (this.apiData.data[value].state === 2) {
          return '<div style="background-color: ' + this.stateColor3 + '; border-radius: 10px; padding: 5px 5px; font-weight: bold;">' + this.myapiData.data[value].value
        }
      }
    },
    update_data () {
      $http.get(this.model)
        .then(x => {
          this.apiData = x.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    print_data () {
      if (this.myapiData) {
        this.apiData = this.myapiData
        // console.log(this.myapiData)
      }
    }
  },
  mounted () {
    this.print_data()
    // this.update_data()
    // setInterval(this.print_data, 1500)
  }
}
</script>

<style>

tr, td {
   border: 1px solid rgb(95, 94, 94);
   background-color: rgb(54, 54, 54);
   color: rgb(223, 222, 222);
}
th {
  display: none;
}
tr:hover td {
  color: #121212;
  background-color: rgb(71, 71, 71);
}
table {
   border: 1px solid rgb(51, 50, 50);
}
</style>