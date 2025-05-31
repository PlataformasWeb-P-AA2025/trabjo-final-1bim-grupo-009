from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion, Publicacion
from configuracion import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Contenido exacto de la publicación cuyas reacciones queremos listar
contenido_publicacion = 'Bukayo Saka del Chelsea dio una asistencia brillante con el estadio lleno.'

# Consulta 2:
# 1. Empezamos desde Reaccion.
# 2. Hacemos join con Publicacion.
# 3. Filtramos por Publicacion.contenido == contenido_publicacion.
reacciones = (
    session.query(Reaccion)
           .join(Reaccion.publicacion)
           .filter(Publicacion.contenido == contenido_publicacion)
           .all()
)

# Imprimimos el resultado
print(f"Reacciones a la publicación:\n\"{contenido_publicacion}\"")
for reaccion in reacciones:
    # Cada reacción tiene asignado un usuario y un tipo de emoción
    print(f"- {reaccion.usuario.nombre}: {reaccion.tipo_emocion}")
