from flask import Flask, config, render_template, jsonify, request
from flask_cors import CORS
import requests
import json
import time
from kpa_backend import DeviceBackend
from types import SimpleNamespace


class ServerBackend(Flask):
    def __init__(self):
        self.host = '10.6.1.86'
        self.port = 5000
        self.device = DeviceBackend(thread_daemon_mode=True)
        self.device.connect()
  
backend = ServerBackend()



app = Flask('name', static_folder="./dist/static", template_folder="./dist")
app.config['JSON_AS_ASCII'] = False
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/power', methods=['POST'])
def kpa_connect():
    with open("./src/json/view_model.json", encoding='utf8') as file:
        try:
            response = json.load(file)
        except Exception as e:
            print(e)
        time.sleep(2)
        print("set voltage function")
        return jsonify(response)


@app.route('/api/button_handler', methods=['POST'])
def buttons_handler():
    print(request.json)
    button_name = request.json.get('button')
    if button_name == 'power_bdd_aim_voltage_btn':
        backend.device.power_set_voltage(module='bdd', voltage=int(request.json.get('state')))
    elif button_name == 'power_bdd_on_id':
        backend.device.bdd.on_off = 1
        backend.device.bdd.voltage_on_off()
    elif button_name == 'power_bdd_off_id':
        backend.device.bdd.on_off = 0
        backend.device.bdd.voltage_on_off()
    
    if button_name == 'be_aim_voltage_btn':
        backend.device.power_set_voltage(module='be', voltage=int(request.json.get('state')))
    elif button_name == 'be_power_off':
        backend.device.be.on_off = 0
        backend.device.be.voltage_on_off()
    elif button_name == 'be_power_on':
        backend.device.be.on_off = 1
        backend.device.be.voltage_on_off()
    
    if button_name == 'dep_zero_voltage':
        print("dep set 0 voltage")
        backend.device.dep_set_voltage(voltage=0)
    elif button_name == 'dep_neg_voltage':
        print("dep set -30 voltage")
        backend.device.dep_set_voltage(voltage=-30)
    elif button_name == 'dep_pos_voltage':
        print("dep set 30 voltage")
        backend.device.dep_set_voltage(voltage=30)
    return jsonify(status="OK")


@app.route('/api/terminal_handler', methods=['POST'])
def terminal_handler():
    print(request.json)
    return jsonify(status="OK")


@app.route('/api/view_model')
def get_view_model():
    with open("./src/json/view_model.json", encoding='utf8') as file:
        try:
            response = json.load(file)
        except Exception as e:
            print(e)
        return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://10.6.1.86:8080/{}'.format(path)).text
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='10.6.1.86')

