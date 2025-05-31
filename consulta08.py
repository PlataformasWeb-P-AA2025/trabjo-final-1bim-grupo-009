# Mostrar la cantidad total de reacciones realizadas por cada usuario
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario
from configuracion import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta sencilla empezando desde Usuario:
# Obtenemos todos los usuarios y, para cada uno, contamos cuántas reacciones tiene
usuarios = session.query(Usuario).all()

print("Cantidad de reacciones por usuario:")
for usuario in usuarios:
    # Usuario.reacciones es la lista de todas las reacciones vinculadas a ese usuario
    total_reacciones = len(usuario.reacciones)
    print(f"- {usuario.nombre}: {total_reacciones}")
