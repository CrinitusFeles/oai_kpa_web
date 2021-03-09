from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
import json
import time

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
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
        return requests.get('http://192.168.31.9:8080/{}'.format(path)).text
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='192.168.31.9')
