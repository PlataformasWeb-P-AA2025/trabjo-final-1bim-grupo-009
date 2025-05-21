import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

# Crear motor y sesión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# === 1. Cargar usuarios ===
df_usuarios = pd.read_csv('DATA/usuarios_red_x.csv', encoding='utf-8')
usuarios = {}

for _, row in df_usuarios.iterrows():
    nombre = row[0].strip()  # La columna no tiene nombre, así que se accede por índice
    if nombre and not session.query(Usuario).filter_by(nombre=nombre).first():
        usuario = Usuario(nombre=nombre)
        session.add(usuario)
        session.flush()  # Asegura que tenga ID para relaciones posteriores
        usuarios[nombre] = usuario

session.commit()

# === 2. Cargar publicaciones ===
df_publicaciones = pd.read_csv('DATA/usuarios_publicaciones.csv', sep='|', encoding='utf-8')
publicaciones = {}

for _, row in df_publicaciones.iterrows():
    nombre_usuario = row['usuario'].strip()
    contenido = row['publicacion'].strip()

    usuario = usuarios.get(nombre_usuario) or session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    if usuario and not session.query(Publicacion).filter_by(contenido=contenido).first():
        publicacion = Publicacion(contenido=contenido, usuario=usuario)
        session.add(publicacion)
        session.flush()
        publicaciones[contenido] = publicacion

session.commit()

# === 3. Cargar reacciones ===
df_reacciones = pd.read_csv('DATA/usuario_publicacion_emocion.csv', sep='|', encoding='utf-8')

for _, row in df_reacciones.iterrows():
    nombre_usuario = row['Usuario'].strip()
    comentario = row['comentario'].strip()
    tipo_emocion = row['tipo emocion'].strip()

    usuario = usuarios.get(nombre_usuario) or session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    publicacion = publicaciones.get(comentario) or session.query(Publicacion).filter_by(contenido=comentario).first()

    if usuario and publicacion:
        reaccion = Reaccion(usuario=usuario, publicacion=publicacion, tipo_emocion=tipo_emocion)
        session.add(reaccion)

session.commit()