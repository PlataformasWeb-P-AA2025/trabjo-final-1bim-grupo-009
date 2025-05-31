from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion, Usuario
from configuracion import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Nombre del usuario para filtrar sus reacciones
nombre_usuario = 'Shelley'

# Consulta:
# 1. Empezamos desde Reaccion.
# 2. Hacemos join con Usuario.
# 3. Filtramos por Usuario.nombre == nombre_usuario.
reacciones = (
    session.query(Reaccion)
           .join(Reaccion.usuario)
           .filter(Usuario.nombre == nombre_usuario)
           .all()
)

# Imprimimos las publicaciones a las que reaccionó el usuario
print(f"Publicaciones a las que {nombre_usuario} ha reaccionado:")
for reaccion in reacciones:
    print(f"- \"{reaccion.publicacion.contenido}\" con emoción: {reaccion.tipo_emocion}")
