import time
import struct
from OAI_modbus import OAI_Modbus


class CfgParameter:
    def __init__(self, **kwargs):
        self.serial_number = kwargs.get('serial_num', '20653699424D')


class OaiMKU:
    def __init__(self, **kwargs):
        self.cfg = CfgParameter(serial_num="20653699424D")

        self.serial_number = kwargs.get('serial_num', '20653699424D')

        self.debug = kwargs.get('debug', False)

        self.client = OAI_Modbus(serial_num=[self.serial_number])
        self.client.debug_print_flag = self.debug

        self.state = 0

        self.low_time = 0x86A0
        self.high_time = 0x0001
        self.GPIO_alternative_set = 1228
        self.GPIO1_12_alternative_set = 1242
        self.GPIO13_28_alternative_set = 1243

    def init(self):
        self.client.ao_read_ranges = [[1228, 1245], [1059, 1063]]
        self.client.write_regs(offset=1060, data_list=[0x1FE0, 0x0000, 0x0000, 0x0000])

    def connect(self, serial_num=None):
        """
        connection to the HW-module
        connection parameter can be updated
        :param serial_num: serial_number
        :return: nothing
        """
        if serial_num:
            self.serial_number = serial_num
            self.client.serial_numbers.append(self.serial_number)
        pass
        if self.client.connect() == 1:
            self.init()
            self.state = 1
        else:
            self.state = -1
        return self.state

    def disconnect(self):
        try:
            if self.client.disconnect() == 0:
                self.state = 0
            else:
                self.state = -1
        except AttributeError:
            self.state = -1
            pass
        return self.state

    def reconnect(self):
        self.disconnect()
        self.connect()

    def impact(self, low_time, high_time, offset, gpio_num):
        """
        Set gpio to output for a specific amount of time
        :param low_time: set time     0x0000[0000]
        :param high_time: set time    0x[0000]0000
        :param gpio_num: number gpio
        :return:
        """

        self.client.write_regs(offset=offset, data_list=[gpio_num])
        self.client.write_regs(offset=self.GPIO_alternative_set,
                               data_list=[0x0001, 0x0001, 0x0000, 0x0000, 0x0000, low_time, high_time, 0x0000, 0x0000])

    def on_gpio(self, offset, ao_register_map):
        """
            Set gpio to output
        :param offset: register number
        :param ao_register_map: register map
        :return:
        """
        self.client.write_ranges = ao_register_map
        self.client.write_regs(offset, ao_register_map)

    def off_gpio(self, offset):
        """
            Set all gpio in register to input
        :param offset: register number
        :return:
        """
        self.client.write_regs(offset, [0x1000, 0x0000, 0x0000, 0x0000])

    def tk_on(self):
        """ 
            gpio1
            ???? ???????????? ???? ?????? / ?? ??2 ????"????????. ??????"(-) 5,6 ??????
        :return: 
        """
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0800)

    def tk_off(self):
        """
            gpio2
            ???? ???????????? ???? ???????? / ?? ??2 ????"????????. ??????"(-) 7,8 ??????
        :return:
        """
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0400)

    def mrk_on(self):
        """
            gpio3
            ???? ???????????? ?????? ?????? / ??2 ??????"??????. ??????"(-) 9,10 ??????
        :return:
        """
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0200)

    def mrk_off(self):
        """
            gpio4
            ???? ???????????? ?????? ???????? / ??2 ??????"????????. ??????"(-) 11,12 ??????
        :return:
        """
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0100)

    def pk1_on(self):
        """
            gpio5
            ???? ???????????? ????1 ?????? / ??2 ??????"??????. 2??????"(-) 13,14 ??????
        :return:
        """
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0080)

    def pk2_on(self):
        """
            gpio6
            ???? ???????????? ????2 ?????? / ??2 ??????"??????. 1??????"(-) 15,16 ??????
        :return:
        """
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0040)

    def pk_off(self):
        """
            gpio7
            ???? ???????????? ???? ???????? / ??2 ??????"????????. ??????"(-) 17,18 ??????
        :return:
        """
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0020)

    def gpio_8(self):
        self.impact(low_time=self.low_time, high_time=self.high_time, offset=self.GPIO1_12_alternative_set,
                    gpio_num=0x0010)


if __name__ == '__main__':
    mku = OaiMKU(serial_num="20693699424D", debug=True)
    mku.connect()
    mku.tk_on()
    # mku.tk_off()
    # mku.mrk_on()
    # mku.mrk_off()
    # mku.pk1_on()
    # mku.pk2_on()
    # mku.pk_off()

    # mku.gpio_8()