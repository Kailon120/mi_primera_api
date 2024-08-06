from app.extensions import db
from .models.producto import Producto
from .models.usuarios import User
from flask_jwt_extended import create_access_token
from datetime import timedelta

def inicio_sesion(email,password):
    # Nos asegura que el usuario efectivamente este registrado en la DB
    user = User.get_user_by_email(email=email)

    #Tiempo en el que el token expira
    caducidad = timedelta(minutes=2)

    # Si user no es None y la contrasena hasheada coincide con la DB
    if user and (user.check_password(password=password)):
        #Creamos un token de acceso
        token_acceso = create_access_token(identity=user.username,expires_delta=caducidad)
        return {'Mensaje':'Loggeado',
                'Token': token_acceso
                }, 200
    
    return {'Error': 'Correo o contraseña no existen'}, 400

def user_register(username, email, password):
    # Busca un usuario por su email
    user = User.get_user_by_email(email=email)

    # Si el usuario ya estaba registrado, regresamos un error
    if user is not None:
        return {'Error': 'Este correo ya está registrado :('}, 403
    
    # Se crea un objeto tipo User con el username y un correo
    nuevo_usuario = User(username=username, email=email)
    # A ese objeto se le asigna una contraseña
    nuevo_usuario.set_password(password=password) # <- Se crea una contraseña cifrada
    # Guardamos el user en la DB
    nuevo_usuario.save()

    return {'Nuevo usuario': {
        'email': email,
        'username': username
    }}, 200 # Le damos una respuesta satisfactoria al usuario

# Esta funcion busca un elemento en la DB por ID o por nombre
def buscar_elemento_id_nombre(parametro_id, parametro_nombre):
    # Verificar si el usuario mando como Query el ID
    if parametro_id != None:
        # Obtenemos el producto desde nuestra DB a traves del ID
        producto_obtenido = Producto.query.get_or_404(parametro_id)
        # Creamos un JSON donde mostramos los datos del elemento
        json_retornado = {
            'id': producto_obtenido.id,
            'nombre': producto_obtenido.nombre,
            'cantidad': producto_obtenido.cantidad
        }
        # Retornamos ese JSON para que el usuario lo vea
        return json_retornado

    # Verificar si el usuario mando como Query el nombre
    elif parametro_nombre != None:
        # Buscamos un producto por su nombre y mostramos el primero o 404
        producto_obtenido = Producto.query.filter_by(nombre=parametro_nombre).first_or_404()

        # Creamos un JSON donde mostramos los datos del elemento
        json_retornado = {
            'id': producto_obtenido.id,
            'nombre': producto_obtenido.nombre,
            'cantidad': producto_obtenido.cantidad
        }
        # Retornamos ese JSON para que el usuario lo vea
        return json_retornado
    
    else:
        return {'Error': 'No pusiste ninguna query', 'status':404}
    
def crear_producto(nombre,cantidad):
    nuevo_producto = Producto(nombre = nombre,cantidad = cantidad)
    db.session.add(nuevo_producto)
    db.session.commit()
    # Creamos un JSON donde mostramos los datos del elemento
    json_retornado = {
        'id': nuevo_producto.id,
        'nombre': nuevo_producto.nombre,
        'cantidad': nuevo_producto.cantidad
    }
    # Retornamos ese JSON para que el usuario lo vea
    return json_retornado