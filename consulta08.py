# Mostrar la cantidad total de reacciones realizadas por cada usuario

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion, Usuario
from configuracion import cadena_base_datos 

# Configuración de la conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Realizamos una consulta que une usuarios con sus reacciones
# y cuenta cuántas reacciones ha hecho cada uno.
# Se agrupa por el ID del usuario.
resultados = session.query(
    Usuario.nombre, 
    func.count(Reaccion.publicacion_id)
).join(Reaccion).group_by(Usuario.id).all()

# Imprimimos el resultado con el nombre del usuario y la cantidad de reacciones
print("Cantidad de reacciones por usuario:")
for nombre, total in resultados:
    print(f"- {nombre}: {total}")
