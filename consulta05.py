from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Lista de emociones para filtrar
emociones_filtrar = ['alegre', 'enojado', 'pensativo']
# Tupla con las vocales para excluir nombres que comienzan con estas vocales
vocales = ('A', 'E', 'I', 'O', 'U')

reacciones = session.query(Reaccion).filter(Reaccion.tipo_emocion.in_(emociones_filtrar)).all()

# Recorremos las reacciones filtradas
for re in reacciones:
    # Verificamos que el usuario tenga nombre y que este no comience con una vocal
    if re.usuario and re.usuario.nombre and re.usuario.nombre[0].upper() not in vocales:
        # Imprimimos el nombre del usuario y el tipo de emoción de la reacción
        print(f"{re.usuario.nombre} - {re.tipo_emocion}")
