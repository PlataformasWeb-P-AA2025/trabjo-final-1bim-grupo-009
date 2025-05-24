# Consulta 1 Listar publicaciones de un usuario.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario
from configuracion import cadena_base_datos

# Configuración de la conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Nombre del usuario del cual queremos obtener las publicaciones
nombre_usuario = 'Dustin'  

# Buscamos al usuario en la base de datos
usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()

# Si el usuario existe, mostramos sus publicaciones 
if usuario:
    print(f"Publicaciones de {usuario.nombre}:")
    if usuario.publicaciones:
        for pub in usuario.publicaciones:
            print(f"- {pub.contenido}")
    else:
        print("Este usuario no tiene publicaciones registradas.")
else:
    print("Usuario no encontrado.")
