# Consulta sobre cuántas publicaciones existen en total
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Publicacion
from configuracion import cadena_base_datos

# Crear el motor de conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Hacer la consulta para contar todas las publicaciones
cantidad = session.query(func.count(Publicacion.id)).scalar()

# Imprimir el resultado
print(f"Cantidad total de publicaciones: {cantidad}")
