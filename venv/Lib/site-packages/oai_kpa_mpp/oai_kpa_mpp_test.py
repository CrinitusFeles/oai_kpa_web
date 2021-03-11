import oai_modbus
import threading
import time

if __name__ == '__main__':
   #mpp = oai_modbus.OAI_Modbus(serial_num=['207F369F424D'], debug=True)
    mpp = oai_modbus.OAI_Modbus(serial_num=['206D3699424D'], debug=True)

    mpp.connect()
    """
    GPIO MAP:

    DEP GPIOs :     GPIO 1 = GPIO 1     //      DEP voltage turn-on/turn-off
                    GPIO 3 = GPIO 3     //      -30 voltage turn-on
                    GPIO 7 = GPIO 7     //      +30 voltage turn-on
       """


    def GPIO_initialization():
        """
        Initialization of certain GPIO groups
        :param target: all_slots, usb hubs, external available GPIO pins, all GPIO pins
        :return:    nothing
        """
        mpp.write_regs(1060, [0x1a30, 0x0000, 0x0000, 0x0000])  # GPIOs 1,3,7 initialization


    def DEP_control():
        """
        Set value for certain GPIO groups
        :param data:
        :param value:
        :param target: all_slots, usb hubs, external available GPIO pins, all GPIO pins
        :return: nothing
        """
        mpp.write_regs(1060, [0x1a30, 0x0000, 0x0000, 0x0000])  # GPIOs 1,7 initialization
        while True:
            mpp.write_regs(1064, [0x1a00, 0x0000, 0x0000, 0x0000])  # GPIOs 1,3 set //  current in the coil
            mpp.write_regs(1064, [0x1300, 0x0000, 0x0000, 0x0000])  # GPIOs 1 set //  -30 voltage turn-on
            time.sleep(3)
            mpp.write_regs(1064, [0x1330, 0x0000, 0x0000, 0x0000])  # GPIOs 1,7 set //  current in the coil
            mpp.write_regs(1064, [0x1300, 0x0000, 0x0000, 0x0000])  # GPIOs 1 set //  +30 voltage turn-on
            time.sleep(3)
            mpp.write_regs(1064, [0x1000, 0x0000, 0x0000, 0x0000])  # GPIOs 1,7 set //  DEP voltage turn-off
            time.sleep(3)



    time.sleep(0.1)
    GPIO_initialization()
    DEP_control()

    mpp.disconnect()
