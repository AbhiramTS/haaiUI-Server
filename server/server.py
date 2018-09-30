from flask import Flask, request, jsonify
import fileHandle as init
import toggle as toggle
import sensor as data

app = Flask(__name__)

@app.route("/")
def index():
    pinName = request.args['_pin']
    pinNo = int(pinName[-1])
    toggle.toggle(pinNo)
    return jsonify(request=pinNo)

@app.route("/sensor")
def sense():
    sensorK = request.args['sensor']
    val = data.getData(sensorK)
    return jsonify(value={sensorK, val})


if __name__ == '__main__':
    init.init()
    app.run(port=5000, host="0.0.0.0")