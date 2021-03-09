<template>
    <div class="terminal_widget">
        <div class="terminal">
            <shell 
            v-bind:banner="banner"
            :shell_input="send_to_terminal"
            :commands="commands"
            @shell_output="prompt"> 
            </shell>
        </div>
        <div class="foreground">.</div>
    </div>
</template>

<script>
import shell from './terminal'
import image1 from '../../../assets/terminal_logo_small2.png'
import image2 from '../../../assets/eva-removebg-preview.png'
export default {
  data: function () {
    return {
      send_to_terminal: '',
      commands: [
        {
          name: 'info',
          desc: 'Show information about this terminal',
          get () {
            return `<p style="color: white">With ❤️ By Salah Bentayeb @halasproject.</p>`
          }
        },
        {
          name: 'uname',
          desc: 'Show the current terminal name',
          get () {
            return `<p style="color: white">` + navigator.appVersion + `</p>`
          }
        }
      ],
      banner: {
        header: 'Командная строка БДК2',
        subHeader: 'Прием и передача modbus команд для КПА',
        helpHeader: 'Введите "help" для получения списка команд.',
        emoji: {
          first: '☠️',
          second: '💀',
          time: 750
        },
        sign: 'KPA $',
        img: {
          align: 'left',
          link: image1,
          width: 175,
          height: 210
        }
      }
    }
  },
  components: {
    shell
  },
  methods: {
    prompt (value) {
      if (value.trim() === 'ifconfig') {
        this.send_to_terminal = `
    Wi-Fi wireless network card:
        
    Local link IPv6 address. . . : fe80 :: 340f: 6f02: 41e9: 477b% 24
    IPv4 address. . . . . . . . .: 192.168.1.2
    Subnet mask. . . . . . . . . : 255.255.255.0
    Default Gateway. . . . . . . : 192.168.1.1`
        this.banner.img.link = image1
      } else {
        this.send_to_terminal = `'${value}' is not recognized as an internal command or external,
an executable program or a batch file`
        this.banner.img.link = image2
      }
    }
  }
}
</script>

<style scoped>

.terminal_widget{
    /* min-width: 560px; */
    width: 100%;
}
.foreground{
  top: 50px;
  height: 1300px;
  z-index: -1;
  background-image: url("../../../assets/img-noise-1200x900.png");
  top: 40px;
  position: relative;
  top: -1250px;
  width: 100%;
  border-radius: 30px;
}
.terminal{
  height: 1300px;
  min-width: 560px;
  width: 100%;
  padding: 20px 45px;
}

</style>