from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Publicacion, Usuario
from configuracion import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Nombre del usuario para filtrar sus publicaciones
nombre_usuario = 'Dustin'

# Consulta 1:
# 1. Empezamos desde Publicacion.
# 2. Hacemos join con Usuario.
# 3. Filtramos por Usuario.nombre == nombre_usuario.
publicaciones = (
    session.query(Publicacion)
           .join(Publicacion.usuario)
           .filter(Usuario.nombre == nombre_usuario)
           .all()
)

# Imprimimos los resultados
print(f"Publicaciones de {nombre_usuario}:")
for pub in publicaciones:
    print(f"- {pub.contenido}")
