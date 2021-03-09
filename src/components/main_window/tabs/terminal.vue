<template>
  <div @click="$refs.cmd.focus()">
    
    <div ref="terminal" id="container">

      <div class="scanline"></div>
      
        <div v-if="banner" id="banner">
          <p>
            <img
              v-if="banner.img"
              :align="banner.img.align ? banner.img.align : 'left'"
              alt="Vue logo"
              src="./../../../assets/terminal_logo_small2.png"
              :width="banner.img.width ? banner.img.width : '151px'"
              :height="banner.img.height ? banner.img.height : '120px'"
            />
          </p>
          <glitch v-if="banner.header" style="letter-spacing: 4px; font-size: 60px;" :msg="banner.header"></glitch>
          <p></p>
          <glitch v-if="banner.subHeader" :msg="banner.subHeader" style="font-size: 30px;"></glitch>
          <p></p>
          <glitch v-if="banner.helpHeader" :msg="banner.helpHeader" style="font-size: 30px;"></glitch>
          <p></p>
        </div>
    <div style=" overflow: auto; width: 100%;">
      <div style="height: 900px; width: 90%;">
        <output ref="output" class="output_class"></output>
        <div id="input-line" class="input-line" style="font-size: 20px;">
          <div class="prompt">
            <div v-if="banner.emoji.first && showemoji">({{banner.emoji.first}})</div>
            <div v-if="banner.emoji.second && !showemoji">({{banner.emoji.second}})</div>
            <div>{{banner.sign ? banner.sign : '>>'}}</div>
          </div>

          <input
            v-model="value"
            ref="cmd"
            @keydown.enter="cmd_enter($event)"
            @keydown.up="history_up()"
            @keydown.down="history_down()"
            @keydown.tab="cmd_tab($event)"
            class="cmdline"
            
            style="font-size: 30px;"
          />
        </div>
      </div>
      
    </div>
  </div>
    
  </div>
</template>

<script>
import glitch from './glitch'
import axios from 'axios'

export default {
  components: {
    glitch
  },
  props: {
    shell_input: {
      required: false
    },
    banner: {
      type: Object,
      required: false,
      default: () => {
        return {
          header: 'Vue Shell',
          subHeader: 'Shell is power just enjoy 🔥',
          helpHeader: 'Enter "help" for more information.',
          emoji: {
            first: '🔅',
            second: '🔆',
            time: 750
          },
          sign: 'VueShell $',
          img: {
            align: 'left',
            link: `@/logo.png`,
            width: 100,
            height: 100
          }
        }
      }
    },
    commands: {
      type: Array
    }
  },
  data () {
    return {
      showemoji: true,
      value: '',
      history_: [],
      histpos_: 0,
      histtemp_: 0
    }
  },
  computed: {
    allcommands () {
      var tab = [
        { name: 'help', desc: 'Show all the commands that are available' },
        { name: 'clear', desc: 'Clear the terminal of all output' }
      ]
      if (this.commands) {
        this.commands.forEach(({ name, desc }) => {
          tab.push({ name, desc })
        })
      }
      return tab
    }
  },
  watch: {
    shell_input (val) {
      this.output(val)
      this.$parent.send_to_terminal = ''
    }
  },
  methods: {
    sendData (arg1) {
      axios.post('http://10.6.1.86:5000/api/terminal_handler', arg1)
        .then((response) => {
          console.log(response.data)
          this.output(response.data.status)
        })
        .catch(error => {
          console.log(error)
        })
    },
    history_up () {
      if (this.history_.length) {
        if (this.history_[this.histpos_]) {
          this.history_[this.histpos_] = this.value
        } else {
          this.histtemp_ = this.value
        }
      }
      // up 38
      this.histpos_--
      if (this.histpos_ < 0) {
        this.histpos_ = 0
      }
      this.value = this.history_[this.histpos_]
        ? this.history_[this.histpos_]
        : this.histtemp_
    },
    history_down () {
      if (this.history_.length) {
        if (this.history_[this.histpos_]) {
          this.history_[this.histpos_] = this.value
        } else {
          this.histtemp_ = this.value
        }
      }
      this.histpos_++
      if (this.histpos_ > this.history_.length) {
        this.histpos_ = this.history_.length
      }
      this.value = this.history_[this.histpos_]
        ? this.history_[this.histpos_]
        : this.histtemp_
    },
    cmd_tab (e) {
      e.preventDefault()
    },
    cmd_enter () {
      if (this.value) {
        this.history_[this.history_.length] = this.value
        this.histpos_ = this.history_.length
      }
      //   Duplicate current input and append to output section.
      var line = this.$refs.cmd.parentNode.cloneNode(true)
      line.removeAttribute('id')
      line.classList.add('line')
      var input = line.querySelector('input.cmdline')
      input.autofocus = false
      input.readOnly = true
      this.$refs.output.appendChild(line)
      this.sendData({cmd: this.value})
      if (this.value && this.value.trim()) {
        var args = this.value.split(' ').filter(function (val) {
          return val
        })
        var cmd = args[0].toLowerCase()
        args = args.splice(1) // Remove cmd from arg list.
      }
      if (cmd === 'clear') {
        this.$refs.output.innerHTML = ''
        this.value = ''
      } else if (cmd === 'help') {
        var commandsList = this.allcommands.map(({name, desc}) => {
          if (desc) {
            return `${name}: ${desc}`
          }
          return name
        })
        this.output(
          '<div class="ls-files" style="color: white">' + commandsList.join('<br>') + '</div>'
        )
      } else {
        if (this.commands) {
          this.commands.forEach(a => {
            if (cmd === a.name) {
              this.output(a.get())
            }
          })
        }
        if (this.value.trim() !== '') {
          this.$emit('shell_output', this.value)
        }
        this.value = ''
      }
      // Clear/setup line for next input.
    },
    output (html) {
      this.$refs.output.insertAdjacentHTML(
        'beforeEnd',
        '<pre style="color: white; font-family: VT323; font-size: 25px">' + html + '</pre>'
      )
      this.value = ''
    }
  },
  mounted () {
    if (
      this.banner.emoji.first &&
      this.banner.emoji.second &&
      this.banner.emoji.time
    ) {
      setInterval(() => {
        this.showemoji = !this.showemoji
      }, this.banner.emoji.time)
    }
  }
}
</script>

<style scoped>
::-webkit-scrollbar { width: 3px; height: 3px;}
::-webkit-scrollbar-button {  background-color: #666; }
::-webkit-scrollbar-track {  background-color: #999;}
::-webkit-scrollbar-track-piece { background-color: #ffffff;}
::-webkit-scrollbar-thumb { height: 50px; background-color: #666; border-radius: 3px;}
::-webkit-scrollbar-corner { background-color: #999;}
::-webkit-resizer { background-color: #666;}
@font-face {
    font-family: "VT323";
    src: url("../../../assets/VT323/VT323-Regular.ttf");
}
#container {
  color: white;
  background-color: rgba(0, 0, 0, 0.5);
    background: linear-gradient(
    to bottom,
    rgba(18, 16, 16, 0) 70%,
    rgba(0, 0, 0, 0.25) 10%
    );
    background-size: 100% 7px;
  font-size: 12pt;
  font-family: Inconsolata, monospace;
  padding: 0.5em 1.5em 1em 1em;
  text-align: left;
  text-shadow:0 0 24px #fff;
  font-family: 'VT323';
  height: 200%;
  opacity: 0.7;
  z-index: 2;
}
.scanline {
    width: 100%;
    height: 100px;
    z-index: -10;
    background: linear-gradient(
        0deg,
        rgba(0, 0, 0, 0) 0%,
        rgba(255, 255, 255, 0.2) 10%,
        rgba(0, 0, 0, 0.1) 100%
    );
    opacity: 0.2;
    position: relative;
    bottom: 100%;
    animation: scanline 4s linear infinite;
}
@keyframes scanline {
    0% {
        top: -100px;
    }
    100% {
        top: 1300px;
    }
}
@keyframes textShadow {
  10% {
    text-shadow: 0.4389924193300864px 0 1px rgba(0,30,255,0.5), -0.4389924193300864px 0 1px rgba(255,0,80,0.3), 0 0 3px;
  }
  50% {
    text-shadow: 2.7928974010788217px 0 1px rgba(0,30,255,0.5), -2.7928974010788217px 0 1px rgba(255,0,80,0.3), 0 0 3px;
  }
  /** etc */
}
#container output {
  clear: both;
  width: 100%;
}
#banner {
  margin-bottom: 3em;
}
img {
  margin-right: 20px;
}
.output_class {
  color: white;
  text-shadow:0 0 14px #fff;
  font-size: 25px;
  font-family: 'VT323';
}
.input-line {
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  clear: both;  
  font-size: 25px;
}
.input-line > div:nth-child(2) {
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  background-color: red;
  font-size: 25px;
}
.prompt {
  white-space: nowrap;
  color: #fafafa;
  text-shadow: 0, 0, 2px, white;
  margin-right: 7px;
  display: -webkit-box;
  display: -moz-box;
  display: box;
  box-pack: center;
  box-orient: vertical;
  user-select: none;
  font-size: 30px;
}
.cmdline {
  outline: none;
  background-color: transparent;
  margin: 0;
  width: 100%;
  font: inherit;
  border: none;
  color: inherit; 
  text-shadow:0 0 2px #fff,
  0 0 3px #fff,
  0 0 5px #ff00de;
}
.ls-files {
  height: 45px;
  column-width: 100px;

}

</style>