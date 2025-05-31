# Consulta para mostrar las emociones más utilizadas en las reacciones

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion
from configuracion import cadena_base_datos

# motor de conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta para contar cuántas veces se ha usado cada tipo de emoción
#    - Empezamos desde Reaccion
#    - Agrupamos por tipo_emocion
#    - Contamos cada grupo y lo ordenamos de mayor a menor
resultados = (
    session.query(
        Reaccion.tipo_emocion,
        func.count().label("cantidad")
    )
    .group_by(Reaccion.tipo_emocion)
    .order_by(func.count().desc())
    .all()
)

# Imprimir el reporte de emociones más utilizadas
print("Emociones más utilizadas:")
for emocion, cantidad in resultados:
    print(f"- {emocion}: {cantidad} veces")
