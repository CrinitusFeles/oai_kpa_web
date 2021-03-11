from oai_kpa_stm_data import OaiKpaSTM
from oia_kpa_power_data import OaiKpaPower
from oai_kpa_mpp_data import OaiKpaMPP
from oai_kpa_interface import OaiDigitalModule
import time
import json
import threading


class DeviceBackend:
    def __init__(self, **kwargs):
        self.stm_id = kwargs.get('stm_id', '20713699424D')
        self.bdd_id = kwargs.get('bdd_id', '20643699424D')
        self.be_id = kwargs.get('be_id', '20523688424D')
        self.mku_id = kwargs.get('mku_id', '20713699424D')
        self.dep_id = kwargs.get('dep_id', '207F369F424D')
        self.interface_id = kwargs.get('interface_id', '20703699424D')
        self.write_period_ms = 300
        self.thread_daemon_mode = kwargs.get('thread_daemon_mode', False)

        self.stm = None
        self.bdd = None
        self.be = None
        self.dep = None
        self.mku = None
        self.mko = None
        self.interface = None

        self.parser_thread = None
        self.thread_flag = False

    def connect(self):
        self.stm = OaiKpaSTM(serial_num=self.stm_id)
        self.stm.connect(serial_num=self.stm_id)
        self.bdd = OaiKpaPower(serial_num=self.bdd_id)
        self.bdd.connect(serial_num=self.bdd_id)
        self.bdd.test_init()
        self.be = OaiKpaPower(serial_num=self.be_id)
        self.be.connect(serial_num=self.be_id)
        self.be.test_init()
        self.dep = OaiKpaMPP(serial_num=self.dep_id)
        self.dep.connect()
        self.interface = OaiDigitalModule(serial_num=self.interface_id)
        self.interface.connect()

        self.start_parser_thread()

    def start_parser_thread(self):
        self.parser_thread = threading.Thread(target=self.parser, daemon=self.thread_daemon_mode)
        self.thread_flag = True
        self.parser_thread.start()

    def stop_parser_thread(self):
        self.thread_flag = False
        self.parser_thread = None

    def parser(self):
        while self.thread_flag:
            with open('src/json/view_model.json', 'r+', encoding='utf8') as f:
                d = json.load(f)
                d['stm']['connection_status'] = True if self.stm.state == 1 else False
                stm_data = self.stm.get_channels_values()
                for model_data, stm_value, stm_state in zip(d['stm']['table1']['data'], stm_data[0][:3], stm_data[1][:3]):
                    model_data['value'] = float("{:.2f}".format(stm_value))
                    model_data['state'] = stm_state
                for model_data, stm_value, stm_state in zip(d['stm']['table2']['data'], stm_data[0][3:12], stm_data[1][3:12]):
                    model_data['value'] = float("{:.2f}".format(stm_value))
                    model_data['state'] = stm_state
                for model_data, stm_value, stm_state in zip(d['stm']['table3']['data'], stm_data[0][12:24], stm_data[1][12:24]):
                    model_data['value'] = float("{:.2f}".format(stm_value))
                    model_data['state'] = stm_state


                bdd_voltage = self.bdd.client.ai_register_map[2141] * 0.00125
                bdd_current = self.bdd.client.ai_register_map[2142]
                d['power']['bdd']['connection_status'] = True if self.bdd.state == 1 else False
                d['power']['bdd']['on_state'] = True if self.bdd.on_off == 1 else False
                d['power']['bdd']['voltage'] = float("{:.2f}".format(bdd_voltage))
                d['power']['bdd']['current'] = float(bdd_current)
                d['power']['bdd']['power'] = float("{:.2f}".format(bdd_voltage * bdd_current))

                be_voltage = self.be.client.ai_register_map[2141] * 0.00125
                be_current = self.be.client.ai_register_map[2142]
                d['power']['be']['connection_status'] = True if self.be.state == 1 else False
                d['power']['bdd']['on_state'] = True if self.be.on_off == 1 else False
                d['power']['be']['voltage'] = float("{:.2f}".format(be_voltage))
                d['power']['be']['current'] = be_current
                d['power']['be']['power'] = float("{:.2f}".format(be_voltage * be_current))

                d['dep']['connection_status'] = True if self.dep.state == 1 else False
                
                d['interface']['connection_status'] = True if self.interface.state == 1 else False
                docking_control = self.get_docking_control()
                print(docking_control)
                d['stm']['table4']['data'][0]['value'] = docking_control[0]
                d['stm']['table4']['data'][0]['state'] = docking_control[1]

                f.seek(0)
                json.dump(d, f, indent=4, ensure_ascii=False)
                f.truncate()

                time.sleep(self.write_period_ms / 1000)

    def power_set_voltage(self, module='bdd', voltage=27):
        if module == 'bdd':
            self.bdd.voltage_expected = voltage * 1000
            self.bdd.voltage_set()
        elif module == 'be':
            self.be.voltage_expected = voltage * 1000
            self.be.voltage_set()
        else:
            print("ERROR: 'power_set_voltage' incorrect module")
        with open('src/json/view_model.json', 'r+', encoding='utf8') as f:
            d = json.load(f)
            d['power'][module]['aim_voltage'] = voltage * 1000
            f.seek(0)
            json.dump(d, f, indent=4, ensure_ascii=False)
            f.truncate()

    def dep_set_voltage(self, voltage):
        if voltage == 0 or -30 or 30:
            self.dep.DEP_control(voltage=voltage)
            with open('src/json/view_model.json', 'r+', encoding='utf8') as f:
                d = json.load(f)
                d['dep']['voltage'] = voltage
                f.seek(0)
                json.dump(d, f, indent=4, ensure_ascii=False)
                f.truncate()
        else:
            print("ERROR: dep incorrect voltage: " + voltage)
    
    def get_docking_control(self):
        val = self.interface.get_analog_inputs()[0]
        state = 0
        if val <= 1500:
            state = 2
        elif val > 1500 and val < 3000:
            state = 1
        elif val >= 3000:
            state = 0
        print([val, state])
        return [val, state]




if __name__ == "__main__":
    backend = DeviceBackend()
    backend.connect()
