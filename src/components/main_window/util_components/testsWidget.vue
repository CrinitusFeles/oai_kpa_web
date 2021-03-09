<template>
  <div class="container-fluid">
    <div class="col">
      <div>
        <vue-ellipse-progress :progress="21" :size="100" :thickness="6" >
          <span slot="legend-value">/100</span>
          <p slot="legend-caption">Выполнено</p>
        </vue-ellipse-progress>
      </div>
      <div>
        <button class="mku_button"> Запуск тестирования </button>
        <p v-text="stm_data"></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      stm_data: 'stm data',
      apiData: undefined,
      parsed_data: undefined
    }
  },
  components: {
  },
  methods: {
    update_data () {
    }
  },
  created () {
    this.update_data()
    // setInterval(this.update_data, 2000)
  }
}
</script>

<style scoped>
.container-fluid{
    border: groove;
    background-color: #262833;
    border-radius: 20px;
    color: white;
    margin-bottom: 10px;
    padding: 10px 15px;
    min-width: 350px;
}
</style>