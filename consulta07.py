# Mostrar todas las emociones que ha usado un usuario específico en sus reacciones
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion
from configuracion import cadena_base_datos

# Crear el motor de conexión a la base de datos
engine = create_engine(cadena_base_datos)

# rear la sesión para ejecutar consultas
Session = sessionmaker(bind=engine)
session = Session()

# Definir el nombre del usuario del que queremos obtener las emociones
nombre_usuario = 'Shelley'

# Consultar todas las reacciones hechas por ese usuario
#    Usamos `has` para filtrar por el atributo `nombre` de la relación usuario
reacciones = (
    session.query(Reaccion)
           .filter(Reaccion.usuario.has(nombre=nombre_usuario))
           .all()
)

# 5. Imprimir las emociones utilizadas por el usuario
print(f"Emociones usadas por {nombre_usuario}:")
for reaccion in reacciones:
    print(f"- {reaccion.tipo_emocion}")
