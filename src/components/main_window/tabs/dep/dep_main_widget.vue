<template>
    <div class="parent">
        <div class="div1"> Модуль генерации помех </div>
        <div class="div2"> 
            <tabs>
                <tab title="Канал 1">
                    <div class="dep_tab">
                        <div class="tab_div1"> Тип сигнала </div>
                        <div class="tab_div2"> Параметры сигнала </div>
                        <div class="tab_div3"> Значение </div>
                        <div class="tab_div4"> 
                            <p><input name="dzen" type="radio" value="imp"> Импульсный </p>
                            <p><input name="dzen" type="radio" value="sin"> Синусоидальный </p>
                        </div>
                        <div class="tab_div5"> Амплитуда, В </div>
                        <div class="tab_div6"> </div>
                        <div class="tab_div7"> Период, мкс</div>
                        <div class="tab_div8"> </div>
                        <div class="tab_div9"> Амплитуда, В </div>
                        <div class="tab_div10"> </div>
                        <div class="tab_div11"> Период, мкс </div>
                        <div class="tab_div12"> </div>
                        <div class="tab_div13"> Длительность импульса, мкс</div>
                        <div class="tab_div14"> </div>
                    </div>
                </tab>
                <tab title="Канал 2">
                    <div class="dep_tab">
                        <div class="tab_div1"> </div>
                        <div class="tab_div2"> </div>
                        <div class="tab_div3"> </div>
                        <div class="tab_div4"> </div>
                        <div class="tab_div5"> </div>
                        <div class="tab_div6"> </div>
                        <div class="tab_div7"> </div>
                        <div class="tab_div8"> </div>
                        <div class="tab_div9"> </div>
                        <div class="tab_div10"> </div>
                        <div class="tab_div11"> </div>
                        <div class="tab_div12"> </div>
                        <div class="tab_div13"> </div>
                        <div class="tab_div14"> </div>
                    </div>
                </tab>
            </tabs>
        </div>
        <div class="div3"> <button class="mku_button"> Вкл. Канал 1 </button> </div>
        <div class="div4"> <button class="mku_button"> Вкл. Канал 2 </button> </div>
        <div class="div5"> <button class="mku_button"> Откл. Канал 1 </button> </div>
        <div class="div6"> <button class="mku_button"> Откл. Канал 2 </button> </div>
    </div>
</template>

<script>
import { Tabs, Tab } from 'vue-slim-tabs'
export default {
  components: {
    Tabs, Tab
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
    padding: 0px 20%;
}

.div1 { grid-area: 1 / 1 / 2 / 3; }
.div2 { grid-area: 2 / 1 / 5 / 3; }
.div3 { grid-area: 5 / 1 / 6 / 2; }
.div4 { grid-area: 5 / 2 / 6 / 3; }
.div5 { grid-area: 6 / 1 / 7 / 2; }
.div6 { grid-area: 6 / 2 / 7 / 3; }

.dep_tab {
display: grid;
grid-template-columns: repeat(3, 1fr);
grid-template-rows: 0.5fr repeat(5, 1fr);
grid-column-gap: 4px;
grid-row-gap: 0px;
padding: 0px 20%;
margin-bottom: 100px;
}

.tab_div1 { grid-area: 1 / 1 / 2 / 2; }
.tab_div2 { grid-area: 1 / 2 / 2 / 3; }
.tab_div3 { grid-area: 1 / 3 / 2 / 4; }
.tab_div4 { grid-area: 2 / 1 / 7 / 2; text-align: left;}
.tab_div5 { grid-area: 2 / 2 / 3 / 3; text-align: left;}
.tab_div6 { grid-area: 2 / 3 / 3 / 4; border: groove; background: white; width: 100px;}
.tab_div7 { grid-area: 3 / 2 / 4 / 3; text-align: left;}
.tab_div8 { grid-area: 3 / 3 / 4 / 4; border: groove; background: white; width: 100px;}
.tab_div9 { grid-area: 4 / 2 / 5 / 3; text-align: left;}
.tab_div10 { grid-area: 4 / 3 / 5 / 4; border: groove; background: white; width: 100px;}
.tab_div11 { grid-area: 5 / 2 / 6 / 3; text-align: left;}
.tab_div12 { grid-area: 5 / 3 / 6 / 4; border: groove; background: white; width: 100px;}
.tab_div13 { grid-area: 6 / 2 / 7 / 3; text-align: left;}
.tab_div14 { grid-area: 6 / 3 / 7 / 4; border: groove; background: white; width: 100px;}

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
.mku_button:hover{
    background-color: #53e943; /* Green */
}
.mku_button:focus{
    background-color: #318628; /* Green */
}
</style>