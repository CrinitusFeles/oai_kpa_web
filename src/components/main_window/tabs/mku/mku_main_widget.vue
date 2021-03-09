<template>
    <div class="parent"> 
        <div class="div1"> БЭ </div>
        <div class="div2"> БДД </div>
        <div class="div3"> <button class="mku_button"> ПК1 </button> </div>
        <div class="div4"> <button class="mku_button"> ПК2 </button> </div>
        <div class="div5"> <button class="mku_button"> БДД ВКЛ </button> </div>
        <div class="div6"> <button class="mku_button"> ТК ВКЛ </button> </div>
        <div class="div7"> <button class="mku_button"> ОТКЛ </button> </div>
        <div class="div8"> <button class="mku_button"> БДД ОТКЛ </button> </div>
        <div class="div9"> <button class="mku_button"> ТК ВКЛ </button> </div>
    </div>
</template>

<style scoped>
.parent {
display: grid;
grid-template-columns: repeat(4, 1fr);
grid-template-rows: 0.5fr repeat(2, 1fr);
grid-column-gap: 4px;
grid-row-gap: 0px;
padding: 0px 300px;
}

.div1 { grid-area: 1 / 1 / 2 / 3; }
.div2 { grid-area: 1 / 3 / 2 / 5; }
.div3 { grid-area: 2 / 1 / 3 / 2; }
.div4 { grid-area: 2 / 2 / 3 / 3; }
.div5 { grid-area: 2 / 3 / 3 / 4; }
.div6 { grid-area: 2 / 4 / 3 / 5; }
.div7 { grid-area: 3 / 1 / 4 / 3; }
.div8 { grid-area: 3 / 3 / 4 / 4; }
.div9 { grid-area: 3 / 4 / 4 / 5; }

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