# Mostrar todas las emociones que ha usado un usuario específico en sus reacciones

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion  
from configuracion import cadena_base_datos  

# Configuración de la conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Definimos el nombre del usuario del que queremos obtener las emociones
nombre_usuario = 'Shelley'

# Consultamos todas las reacciones que haya hecho 
# Usamos 'has' para filtrar por el nombre del usuario relacionado
reacciones = session.query(Reaccion).filter(Reaccion.usuario.has(nombre=nombre_usuario)).all()

# Mostramos las emociones encontradas del usuario
print(f"Emociones usadas por {nombre_usuario}:")
for re in reacciones:
    print(f"- {re.tipo_emocion}")
