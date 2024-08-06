# Importamos el modulo "Resource" de la librería flask_restful
from urllib.parse import parse_qs
from flask_restful import Resource

# Importamos los metodos de nuestra API
from .methods import *

# El modulo request nos permite aceptar info de un usuario
from flask import request

from flask_jwt_extended import jwt_required

# Creamos una clase que va a heredar atributos del modulo "Resource"
class HelloWorld(Resource):

    # Este método se va a ejecutar cuando el usuario acceda a cierta ruta
    @jwt_required()
    def get(self):
        # Regresamos un diccionario con el mensaje que queremos mostrar
        return { 'message': 'Hola mundo desde la API', 'status':200}

class Almacen(Resource):

    # Obtenemos la informacion del almacen
    def get(self):

        # Esta variable va a interceptar la informacion de nuestra Query
        parametro_id = request.args.get('id')
        parametro_nombre = request.args.get('nombre')

        return buscar_elemento_id_nombre(parametro_id, parametro_nombre)

    # Ponemos un nuevo objeto en el almacen
    # Enviarle informacion API mediante el cliente
    def post(self):

        # Se crea una nueva variable para guardar la informacion que posteo el usuario
        data = request.get_json()

        return crear_producto(data['nombre'],data['cantidad'])

class User_register(Resource):
    def post(self):
        data_recieve = request.form
        username = data_recieve.get('username')
        email = data_recieve.get('email')
        password = data_recieve.get('password')

        #print(email,username,password)

        respuesta,status = user_register(username, email, password)
        return respuesta, status

class User_login(Resource):
    def post(self):
        data_recieve = request.form
        email = data_recieve.get('email')
        password = data_recieve.get('password')

        repuesta, status = inicio_sesion(email, password)

        return repuesta,status

# Creamos una clase que va a manejar todas las rutas
class APIRoutes:

    #Se declara un método para inicializar las rutas
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')

        api.add_resource(User_login,'/usuarios/login')

        api.add_resource(User_register,'/usuarios/registro')

        api.add_resource(Almacen, '/objetos_almacen')