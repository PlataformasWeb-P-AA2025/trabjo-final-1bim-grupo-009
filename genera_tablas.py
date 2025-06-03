from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Importamos la cadena de conexión desde el archivo de configuración
from configuracion import cadena_base_datos

# Se crea el motor de conexión con la base de datos
engine = create_engine(cadena_base_datos)

# Se declara la clase base de la que heredarán todas las clases ORM
Base = declarative_base()

# Definición de la clase Usuario que representa la tabla 'usuario'
class Usuario(Base):
    __tablename__ = 'usuario' 

    id = Column(Integer, primary_key=True)  
    nombre = Column(String(50), unique=True, nullable=False)

    # Relación uno a muchos con publicaciones y reacciones
    publicaciones = relationship("Publicacion", back_populates="usuario")
    reacciones = relationship("Reaccion", back_populates="usuario")

# Definición de la clase Publicacion que representa la tabla 'publicacion'
class Publicacion(Base):
    __tablename__ = 'publicacion'  

    id = Column(Integer, primary_key=True)  
    contenido = Column(Text, unique=True, nullable=False)  
    usuario_id = Column(Integer, ForeignKey('usuario.id'))  

    # Relación con el usuario autor y con las reacciones recibidas
    usuario = relationship("Usuario", back_populates="publicaciones")
    reacciones = relationship("Reaccion", back_populates="publicacion")

# Definición de la clase Reaccion que representa la tabla 'reaccion'
class Reaccion(Base):
    __tablename__ = 'reaccion'  # Nombre de la tabla

    # Clave compuesta por usuario_id y publicacion_id
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    publicacion_id = Column(Integer, ForeignKey('publicacion.id'), primary_key=True)
    tipo_emocion = Column(String(50), nullable=False)  # Tipo de emoción (obligatorio)

    # Relación con el usuario que reacciona y la publicación reaccionada
    usuario = relationship("Usuario", back_populates="reacciones")
    publicacion = relationship("Publicacion", back_populates="reacciones")

# Crea todas las tablas en la base de datos a partir de las clases definidas
Base.metadata.create_all(engine)