from flask import Flask
from shutter_i2c import ShuttersController

app = Flask(__name__)


shutter_controller = None


@app.route('/')
def index():
    return "Hello world !"


@app.route('/api/shutter/<int:id>/up')
def shutter_up(id):
    shutter_controller.shutter_up(id)
    return "ok"


@app.route('/api/shutter/<int:id>/down')
def shutter_down(id):
    shutter_controller.shutter_down(id)
    return "ok"


@app.route('/api/shutter/group/<int:id>/up')
def shutter_special_up(id):
    shutter_controller.shutter_group_up(id)
    return "ok"


@app.route('/api/shutter/group/<int:id>/down')
def shutter_special_down(id):
    shutter_controller.shutter_group_down(id)
    return "ok"


@app.route('/api/shutter/alldown')
def shutter_all_down():
    shutter_controller.shutter_all_down()
    return "ok"


@app.route('/api/shutter/allup')
def shutter_all_up():
    shutter_controller.shutter_all_up()
    return "ok"


if __name__ == "__main__":
    shutter_controller = ShuttersController()
    app.run(host='0.0.0.0')
