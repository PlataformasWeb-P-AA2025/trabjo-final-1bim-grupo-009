# Consulta para mostrar los usuarios que no tienen publicaciones asociadas

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario  
from configuracion import cadena_base_datos  

# Configuración de la conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta que obtiene todos los usuarios que NO tienen publicaciones
# Se usa el operador ~ (negación) y el método any() para filtrar
usuarios = session.query(Usuario).filter(~Usuario.publicaciones.any()).all()

# Mostrar los nombres de los usuarios que no han realizado publicaciones
print("Usuarios sin publicaciones:")
for usuario in usuarios:
    print(f"- {usuario.nombre}")
