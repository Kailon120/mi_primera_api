# Importamos el modulo "Resource" de la librería flask_restful
from urllib.parse import parse_qs
from flask_restful import Resource

# El modulo request nos permite aceptar info de un usuario
from flask import request

lista_objetos_almacen = [
    {'id':1,
     'nombre': 'Lapiz',
     'cantidad': 4
    },
    {'id':2,
     'nombre': 'Goma',
     'Cantidad': 3

    },
    {'id':1,
     'nombre': 'Tijera',
     'cantidad': 6
    }]

# Creamos una clase que va a heredar atributos del modulo "Resource"
class HelloWorld(Resource):

    # Este método se va a ejecutar cuando el usuario acceda a cierta ruta
    def get(self):
        # Regresamos un diccionario con el mensaje que queremos mostrar
        return { 'message': 'Hola mundo desde la API', 'status':200}

class Almacen(Resource):

    # Obtenemos la informacion del almacen
    def get(self):

        # Esta variable va a interceptar la informacion de nuestra Query
        parametro_id = request.args.get('id')
        parametro_nombre = request.args.get('nombre')

        # Comparamos si el parametro esta vacio
        if parametro_id != None:
            # Recorremos la lista de objetos en el almacen
            for objeto in lista_objetos_almacen:
                # Si la llave 'id' de un objeto coincide con lo que nos pide el usuario
                if objeto.get('id') == int(parametro_id):
                    #Regresamos el objeto que pidio
                    return {'Objeto': objeto, 'status':200}
            # Si no encuentra coincidencia, le da un mensaje de no encontrada
            return {'Mensaje': 'Objeto no encontrado', 'status': 404}
        
        elif parametro_nombre != None:
            # Recorremos la lista de objetos en el almacen
            for objeto in lista_objetos_almacen:
                # Si la llave 'nombre' de un objeto coincide con lo que nos pide el usuario
                if objeto.get('nombre') == parametro_nombre:
                    #Regresamos el objeto que pidio
                    return {'Objeto': objeto, 'status':200}
            # Si no encuentra coincidencia, le da un mensaje de no encontrada
            return {'Mensaje': 'Objeto no encontrado', 'status': 404}
        
        # Si el parametro no se mando, regresamos todos los objetos de mi lista
        return {'Objetos': lista_objetos_almacen, 'status':200}

    # Ponemos un nuevo objeto en el almacen
    # Enviarle informacion API mediante el cliente
    def post(self):

        # Se crea una nueva variable para guardar la informacion que posteo el usuario
        data = request.get_json()

        # Agregamos la informacion a la lista del almacen
        lista_objetos_almacen.append(data)

        return { 'received': True, 'status':200, 'info': data}

# Creamos una clase que va a manejar todas las rutas
class APIRoutes:

    #Se declara un método para inicializar las rutas
    def init_routes(self, api):
        api.add_resource(HelloWorld, '/')

        api.add_resource(Almacen, '/objetos_almacen')