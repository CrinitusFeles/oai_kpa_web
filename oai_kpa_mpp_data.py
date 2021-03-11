import time
import threading
from OAI_modbus import OAI_Modbus
import json


class CfgParameter:
    def __init__(self, **kwargs):
        self.serial_number = kwargs.get('serial_num', '207F369F424D')


class OaiKpaMPP:
    def __init__(self, *args, **kwargs):
        # объект с параметрами
        self.cfg = CfgParameter(serial_num="207F369F424D")
        
        # разбор именованных параметров
        self.serial_number = kwargs.get('serial_num', '207F369F424D')
        self.debug = kwargs.get('debug', False)
        # создание объекта для общения по МодБас
        self.client = OAI_Modbus(serial_num=[self.serial_number])
        self.client.debug_print_flag = True
        # параметры связи
        self.state = 0
        

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

    def DEP_control(self, voltage):
        """
        :param voltage: voltage
        :return: nothing
        """
        self.client.write_regs(1060, [0x1a30, 0x0000, 0x0000, 0x0000])  # GPIOs 1,7 initialization

        if voltage == 30:
            self.client.write_regs(1064, [0x1330, 0x0000, 0x0000, 0x0000])  # GPIOs 1,7 set //  current in the coil
            self.client.write_regs(1064, [0x1300, 0x0000, 0x0000, 0x0000])  # GPIOs 1 set //  +30 voltage turn-on

        elif voltage == -30:
            self.client.write_regs(1064, [0x1a00, 0x0000, 0x0000, 0x0000])  # GPIOs 1,3 set //  current in the coil
            self.client.write_regs(1064, [0x1300, 0x0000, 0x0000, 0x0000])  # GPIOs 1 set //  -30 voltage turn-on

        elif voltage == 0:
            self.client.write_regs(1064, [0x1000, 0x0000, 0x0000, 0x0000])  # GPIOs 1,7 set //  DEP voltage turn-off




if __name__ == '__main__':
    print("need to create main test script")