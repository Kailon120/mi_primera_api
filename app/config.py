class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:12345@127.0.0.1:5432/mi_almacen'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '2bcdd476bb36a8dd7fa8d209'
    JWT_ALGORITHM = 'HS256'