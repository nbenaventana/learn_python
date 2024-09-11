import pymongo
from datetime import datetime

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://mongo:FBUgdGWPvFqzuQABMwShZTcTwZNrUPQC@autorack.proxy.rlwy.net:31753")
db = client["test"]  # Base de datos "blog"
posts_collection = db["prueba"]  # Colección "posts"

# Función para crear un nuevo post
def crear_post(titulo, contenido, autor_nombre, autor_email, etiquetas):
    post = {
        "titulo": titulo,
        "contenido": contenido,
        "fecha_publicacion": datetime.utcnow(),  # Fecha actual UTC
        "autor": {
            "nombre": autor_nombre,
            "email": autor_email
        },
        "comentarios": [],  # Inicialmente sin comentarios
        "etiquetas": etiquetas
    }
    result = posts_collection.insert_one(post)
    print(f"Post creado con ID: {result.inserted_id}")

# Función para obtener todos los posts
def obtener_posts():
    posts = posts_collection.find()
    for post in posts:
        print(post)

# Función para buscar posts por etiqueta
def buscar_posts_por_etiqueta(etiqueta):
    posts = posts_collection.find({"etiquetas": etiqueta})
    for post in posts:
        print(post)
        print("Titulo: ", post["titulo"])

# Función para buscar posts por coincidencia parcial en las etiquetas
def buscar_posts_por_etiqueta_parcial(busqueda_parcial):
    # Crear expresión regular para búsqueda parcial insensible a mayúsculas/minúsculas
    regex = re.compile(busqueda_parcial, re.IGNORECASE)

    # Realizar la consulta utilizando $regex
    posts = posts_collection.find({"etiquetas": {"$regex": regex}})

    for post in posts:
        print(post)

# Ejemplo de uso
crear_post("Mi primer post", "Contenido del primer post...", "Juan", "juan@ejemplo.com", ["python", "tecnología"])
obtener_posts()
buscar_posts_por_etiqueta("python")
