from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion
from configuracion import cadena_base_datos

# Configuración de la conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Realizamos una consulta que agrupa las reacciones por tipo de emoción
# y cuenta cuántas veces aparece cada una, ordenándolas de mayor a menor
reporte = session.query(Reaccion.tipo_emocion, func.count().label("cantidad"))\
                 .group_by(Reaccion.tipo_emocion)\
                 .order_by(func.count().desc()).all()

# Mostramos los resultados del reporte
print("Reporte de reacciones por tipo:")
for tipo, cantidad in reporte:
    print(f"- {tipo}: {cantidad} veces")
