# Importamos la instancia de nuestra DB
from app.extensions import db

class Producto(db.Model):
    __tablename__ = 'objetos_almacen'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'