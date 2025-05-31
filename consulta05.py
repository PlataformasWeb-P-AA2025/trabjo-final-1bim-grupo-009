from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion
from configuracion import cadena_base_datos

# Crear el motor y la sesión para conectar con la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Definir las emociones que queremos incluir y las vocales a excluir
emociones_filtrar = ['alegre', 'enojado', 'pensativo']
vocales = ('A', 'E', 'I', 'O', 'U')

# Obtener todas las reacciones cuyo tipo esté en nuestra lista
reacciones = session.query(Reaccion) \
                   .filter(Reaccion.tipo_emocion.in_(emociones_filtrar)) \
                   .all()

# Recorrer las reacciones filtradas
for reaccion in reacciones:
    # 4.1 Comprobar que exista un usuario asociado y que su nombre no empiece con vocal
    if reaccion.usuario and reaccion.usuario.nombre and reaccion.usuario.nombre[0].upper() not in vocales:
        # 4.2 Imprimir el nombre del usuario y el tipo de emoción
        print(f"{reaccion.usuario.nombre} - {reaccion.tipo_emocion}")
