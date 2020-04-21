from flask import Flask
from flask import render_template
from flask_fontawesome import FontAwesome
from shutter_i2c import ShuttersController

app = Flask(__name__)
fa = FontAwesome(app)

shutter_controller = ShuttersController()


@app.route('/')
def index():
    return render_template('index.html', shutters=shutter_controller.shutters)


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
    print("Bob")
    shutter_controller = ShuttersController()
    print(shutter_controller)
    app.run(host='0.0.0.0')
