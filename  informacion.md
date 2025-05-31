# 1 Prompt para tener ideas de como poder ingresar datos

Hola ChatGPT, necesito ideas para escribir un script en Python que lea datos desde archivos CSV y los inserte correctamente en mi base de datos usando SQLAlchemy. Tengo tres tablas principales: `Usuario`, `Publicacion` y `Reaccion`. Quiero sugerencias de pasos y buenas prácticas para hacer lo siguiente:

1. Leer un CSV de usuarios (por ejemplo, `usuarios_red_x.csv`), limpiar nombres (quitar espacios), verificar si el usuario ya existe en la base de datos y, si no existe, crearlo.  
2. Leer otro CSV de publicaciones (por ejemplo, `usuarios_publicaciones.csv` con separador `|`), para cada fila buscar al usuario correspondiente (creado o existente), comprobar que la publicación no se duplique y, si no existe, insertarla asociada al usuario.  
3. Leer un tercer CSV de reacciones (por ejemplo, `usuario_publicacion_emocion.csv` con separador `|`), donde cada fila contiene el nombre de usuario, el contenido de la publicación y el tipo de emoción. Para cada fila, buscar tanto el usuario como la publicación en la base de datos (o en diccionarios locales para optimizar), y si ambos existen crear el registro de `Reaccion`.  
4. Usar diccionarios Python para mantener en memoria las instancias ya creadas (usuarios y publicaciones) y así evitar hacer consultas redundantes a la base de datos en cada iteración.  
5. Aconsejarme cómo organizar las carpetas y nombrar los archivos (por ejemplo, `ingresa_usuarios.py`, `ingresa_publicaciones.py`, `ingresa_reacciones.py`) para un flujo limpio y modular.  
6. Sugerir cómo manejar errores comunes (por ejemplo, filas mal formateadas, caracteres especiales, campos vacíos) usando `try/except` o validaciones antes de añadir a la sesión.  
7. Recomendar prácticas para hacer `session.commit()` de forma eficiente (por 
8. Incluir ejemplos de cómo cargar con `pandas.read_csv`, iterar con `df.iterrows()`, limpiar cadenas con `.strip()`, y luego usar `session.query(...)` junto con `session.add(...)` para insertar nuevos objetos.  


# 2 Prompt para generar ideas para hacer consultas a la base 

Hola ChatGPT, estoy trabajando con una base de datos que tiene las tablas `Usuario`, `Publicacion` y `Reaccion`, y quiero generar ideas para crear consultas útiles en SQLAlchemy. Dame ejemplos de consultas relacionadas con estos modelos.

# Respuesta

1. ¿Cómo contar cuántas publicaciones existen en total?  
2. ¿Cómo listar todas las emociones que ha usado un usuario específico en sus reacciones?  
3. ¿Cómo mostrar la cantidad total de reacciones realizadas por cada usuario?  
4. ¿Cómo obtener un reporte de las emociones más utilizadas en todas las reacciones?  
5. ¿Cómo listar los usuarios que no tienen publicaciones asociadas?

