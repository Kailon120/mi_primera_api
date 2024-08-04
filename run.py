#Importamos el servidor montado
from app import crear_app

# Lo ponemos a correr
crear_app().run(debug=True, port=5050)