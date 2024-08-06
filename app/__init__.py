# Importamos la libreria flask
from flask import Flask
from flask_restful import Api
from .routes import APIRoutes
from .config import Config
from .extensions import db, jwt

# Creamos una función para correr el servidor
def crear_app():
    # la variable app contendra todo nuestro servidor
    app = Flask(__name__)

    # Le indicamos a nuestra app que se configura a traves de un objeto
    app.config.from_object(Config)

    # Conectamos la App con la base de datos
    db.init_app(app)

    # Conectamos la app con JWT
    jwt.init_app(app)

    # Antes de que se cree el acceso a la API se ejecutan los siguientes procesos
    with app.app_context():
        # Inicializamos la DB
        db.create_all()

        # La variable API manejara todas las peticiones hacia nuestro servidor
        api = Api(app)

        # Agregamos una variable para manejar las rutas
        routes = APIRoutes()

        # Inicializamos las rutas en nuestra API
        routes.init_routes(api)

    # Regresamos ese servidor montado
    return app