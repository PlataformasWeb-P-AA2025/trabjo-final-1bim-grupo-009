from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion
from configuracion import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Empezamos desde Reaccion.
# grupamos por tipo_emocion y contamos cada grupo.
# Ordenamos de mayor a menor por la cantidad.
reporte = (
    session.query(
        Reaccion.tipo_emocion,
        func.count().label("cantidad")
    )
    .group_by(Reaccion.tipo_emocion)
    .order_by(func.count().desc())
    .all()
)

# Imprimimos el reporte
print("Reporte de reacciones por tipo:")
for tipo, cantidad in reporte:
    print(f"- {tipo}: {cantidad} veces")
