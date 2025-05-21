from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)

    publicaciones = relationship("Publicacion", back_populates="usuario")
    reacciones = relationship("Reaccion", back_populates="usuario")

    def _repr_(self):
        return "Usuario: nombre=%s" % self.nombre

class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    contenido = Column(Text, unique=True, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    usuario = relationship("Usuario", back_populates="publicaciones")
    reacciones = relationship("Reaccion", back_populates="publicacion")

    def _repr_(self):
        return "Publicacion: contenido=%s - autor=%s" % (
            self.contenido,
            self.usuario.nombre if self.usuario else "Desconocido"
        )

class Reaccion(Base):
    __tablename__ = 'reaccion'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    publicacion_id = Column(Integer, ForeignKey('publicacion.id'), primary_key=True)
    tipo_emocion = Column(String(50), nullable=False)

    usuario = relationship("Usuario", back_populates="reacciones")
    publicacion = relationship("Publicacion", back_populates="reacciones")

    def _repr_(self):
        return "Reaccion: usuario=%s - publicacion=%s - emocion=%s" % (
            self.usuario.nombre,
            self.publicacion.contenido,
            self.tipo_emocion
        )

Base.metadata.create_all(engine)