<template>
    <div class="parent">
        <div class="div1"> </div>
        <div class="div2"> Текущее напряжение, В </div>
        <div class="div3"> <button class="mku_button"> ВКЛ </button> </div>
        <div class="div4"> </div>
        <div class="div5"> Текущий ток, мА </div>
        <div class="div6"> <button class="mku_button"> ОТКЛ </button></div>
        <div class="div7"> <NumberInputSpinner
            :min="0"
            :max="10"
            :step="2"
            :integerOnly="true"
            />
        </div>
        <div class="div8"> Желаемое напряжение, В </div>
        <div class="div9"> <button class="mku_button"> Установить напряжение </button> </div>
        <div class="div10"> <NumberInputSpinner
            :min="0"
            :max="10"
            :step="2"
            :integerOnly="true"
            />
        </div>
        <div class="div11"> Калибровка модуля 1 (верхний), мВ </div>
        <div class="div12"> <button class="mku_button"> Задать калибровки </button></div>
        <div class="div13"> <NumberInputSpinner
            :min="0"
            :max="10"
            :step="2"
            :integerOnly="true"
            />
        </div>
        <div class="div14"> Калибровка модулья 2 (нижний), мВ </div>
        <div class="div15"> <button class="mku_button"> Считать калибровки </button> </div>
        <div class="div16"> <NumberInputSpinner
            :min="0"
            :max="10"
            :step="2"
            :integerOnly="true"
            />
        </div>
        <div class="div17"> Ограничение по току, мА </div>
        <div class="div18"> <button class="mku_button"> Задать ограничения </button> </div>
        <div class="div19"> <NumberInputSpinner
            :min="0"
            :max="10"
            :step="2"
            :integerOnly="true"
            />
        </div>
        <div class="div20"> Ограничение по напряжению, В </div>
        <div class="div21"> <button class="mku_button"> Считать ограничения </button> </div>
    </div>
</template>

<script>
import NumberInputSpinner from 'vue-number-input-spinner'

export default {
  components: {
    NumberInputSpinner
  },
  data () {
    return {
      message: 'voltage'
    }
  },
  methods: {
  },
  created () {
  }
}
</script>

<style scoped>
.parent {
display: grid;
grid-template-columns: repeat(3, 1fr);
grid-template-rows: repeat(7, 1fr);
grid-column-gap: 4px;
grid-row-gap: 0px;
padding: 0px 300px;
}

.div1 { grid-area: 1 / 1 / 2 / 2; border: groove; background: white;}
.div2 { grid-area: 1 / 2 / 2 / 3; }
.div3 { grid-area: 1 / 3 / 2 / 4; }
.div4 { grid-area: 2 / 1 / 3 / 2; border: groove; background: white;}
.div5 { grid-area: 2 / 2 / 3 / 3; }
.div6 { grid-area: 2 / 3 / 3 / 4; }
.div7 { grid-area: 3 / 1 / 4 / 2; }
.div8 { grid-area: 3 / 2 / 4 / 3; }
.div9 { grid-area: 3 / 3 / 4 / 4; }
.div10 { grid-area: 4 / 1 / 5 / 2; }
.div11 { grid-area: 4 / 2 / 5 / 3; }
.div12 { grid-area: 4 / 3 / 5 / 4; }
.div13 { grid-area: 5 / 1 / 6 / 2; }
.div14 { grid-area: 5 / 2 / 6 / 3; }
.div15 { grid-area: 5 / 3 / 6 / 4; }
.div16 { grid-area: 6 / 1 / 7 / 2; }
.div17 { grid-area: 6 / 2 / 7 / 3; }
.div18 { grid-area: 6 / 3 / 7 / 4; }
.div19 { grid-area: 7 / 1 / 8 / 2; }
.div20 { grid-area: 7 / 2 / 8 / 3; }
.div21 { grid-area: 7 / 3 / 8 / 4; }

.mku_button{
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    font-size: 12px;
    padding: 8px 5px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    margin-bottom: 10px;
    width: 100%;
}
</style>