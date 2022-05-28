from application_server.rest_http.app import app
from config.environment import APP_PORT, APP_HOST

from .controllers import index


def __main__():
    app.run(host=APP_HOST, debug=True, port=APP_PORT)
