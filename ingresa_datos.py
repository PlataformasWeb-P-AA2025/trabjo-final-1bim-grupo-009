import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

# Motor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 1. Cargar usuarios
# Leer archivo CSV de usuarios
df_usuarios = pd.read_csv('DATA/usuarios_red_x.csv', encoding='utf-8')
usuarios = {}  # Diccionario para guardar instancias de usuarios creados

for _, row in df_usuarios.iterrows():
    nombre = row.iloc[0].strip()  # Acceder correctamente por posición, limpiando espacios del nombre
    # Verificar si el usuario ya existe en la base antes de crearlo
    if nombre and not session.query(Usuario).filter_by(nombre=nombre).first():
        usuario = Usuario(nombre=nombre)  # Crear nueva instancia de Usuario
        session.add(usuario)
        session.flush()  # Guardar temporalmente para obtener su ID
        usuarios[nombre] = usuario  # Guardar en el diccionario

session.commit()  

# 2. Cargar publicaciones 
# Leer archivo CSV de publicaciones con separador personalizado
df_publicaciones = pd.read_csv('DATA/usuarios_publicaciones.csv', sep='|', encoding='utf-8')
publicaciones = {}  # Diccionario para guardar publicaciones por su contenido

for _, row in df_publicaciones.iterrows():
    nombre_usuario = row['usuario'].strip()
    contenido = row['publicacion'].strip()

    # Buscar el usuario en el diccionario o en la base
    usuario = usuarios.get(nombre_usuario) or session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    # Evitar duplicados de publicaciones
    if usuario and not session.query(Publicacion).filter_by(contenido=contenido).first():
        publicacion = Publicacion(contenido=contenido, usuario=usuario)
        session.add(publicacion)
        session.flush()  # Guardar temporalmente para usar luego
        publicaciones[contenido] = publicacion  # Guardar en el diccionario

session.commit()  

# 3. Cargar reacciones
# Leer archivo CSV con reacciones
df_reacciones = pd.read_csv('DATA/usuario_publicacion_emocion.csv', sep='|', encoding='utf-8')

for _, row in df_reacciones.iterrows():
    nombre_usuario = row['Usuario'].strip()
    comentario = row['comentario'].strip()
    tipo_emocion = row['tipo emocion'].strip()

    # Buscar usuario y publicación en los diccionarios o en la base
    usuario = usuarios.get(nombre_usuario) or session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    publicacion = publicaciones.get(comentario) or session.query(Publicacion).filter_by(contenido=comentario).first()

    # Crear reacción solo si se encontró tanto usuario como publicación
    if usuario and publicacion:
        reaccion = Reaccion(usuario=usuario, publicacion=publicacion, tipo_emocion=tipo_emocion)
        session.add(reaccion)

session.commit()  
