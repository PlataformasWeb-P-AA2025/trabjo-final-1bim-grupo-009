# Consulta 2 Listar las reacciones a una publicación.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Publicacion
from configuracion import cadena_base_datos

# Configuración de la conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

contenido_publicacion = 'Bukayo Saka del Chelsea dio una asistencia brillante con el estadio lleno.' 
publicacion = session.query(Publicacion).filter_by(contenido=contenido_publicacion).first()

if publicacion:
    print(f"Reacciones a la publicación: \"{publicacion.contenido}\"")
    for re in publicacion.reacciones:
        print(f"- {re.usuario.nombre}: {re.tipo_emocion}")
else:
    print("Publicación no encontrada.")
