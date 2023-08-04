import eventlet

from project import create_app, ext_celery, socketio


app = create_app()
celery = ext_celery.celery
eventlet.monkey_patch()

@app.route("/")
def hello_world():
    return "Hello world!"


if __name__ == '__main__':
    socketio.run(
        app,
        allow_unsafe_werkzeug=True,
        debug=True,
        use_reloader=True,
        host='0.0.0.0',
    )