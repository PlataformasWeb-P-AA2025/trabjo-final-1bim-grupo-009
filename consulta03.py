# Mostrar en qué publicaciones reaccionó un usuario.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario
from configuracion import cadena_base_datos

# Configuración de la conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Nombre del usuario del cual queremos ver sus reacciones
nombre_usuario = 'Shelley'

# Buscamos al usuario en la base
usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()

# Si el usuario existe muestra todas las publicaciones a las que ha reaccionado
if usuario:
    print(f"{usuario.nombre} ha reaccionado a las siguientes publicaciones:")
    for re in usuario.reacciones:
        print(f"- \"{re.publicacion.contenido}\" con emoción: {re.tipo_emocion}")
else:
    print("Usuario no encontrado.")
