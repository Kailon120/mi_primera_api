# Importamos la libreria flask
from flask import Flask
from flask_restful import Api
from .routes import APIRoutes

# Creamos una función para correr el servidor
def crear_app():
    app = Flask(__name__)
    api = Api(app)

    routes = APIRoutes()
    routes.init_routes(api)

    # Regresamos ese servidor montado
    return app