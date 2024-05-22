# Importar la base de datos desde el archivo de conexión
from conexion import db
from conexion import app
app.app_context().push()


# Definir el modelo de la tabla Pregunta
class Pregunta(db.Model):
    # Definir la columna id como clave primaria
    id = db.Column(db.Integer, primary_key=True)
    # Definir la columna pregunta como tipo String con longitud máxima de 200 caracteres, no puede ser nula
    pregunta = db.Column(db.String(200), nullable=False)
    # Definir la columna respuesta_correcta como tipo String con longitud máxima de 100 caracteres, no puede ser nula
    respuesta_correcta = db.Column(db.String(100), nullable=False)
    # Definir la columna respuesta_incorrecta1 como tipo String con longitud máxima de 100 caracteres, no puede ser nula
    respuesta_incorrecta1 = db.Column(db.String(100), nullable=False)
    # Definir la columna respuesta_incorrecta2 como tipo String con longitud máxima de 100 caracteres, no puede ser nula
    respuesta_incorrecta2 = db.Column(db.String(100), nullable=False)

# Crear la base de datos

    # Crear todas las tablas definidas en el modelo
    db.create_all()

# Importar la aplicación y la base de datos desde el archivo de conexión

        # Verificar si la tabla Pregunta está vacía
if not Pregunta.query.first():
            # Crear una lista de preguntas
            preguntas = [
                Pregunta(
                    pregunta="¿Cuál es la capital de Francia?",
                    respuesta_correcta="París",
                    respuesta_incorrecta1="Londres",
                    respuesta_incorrecta2="Madrid"
                ),
                Pregunta(
                    pregunta="¿Cuántos continentes hay en el mundo?",
                    respuesta_correcta="7",
                    respuesta_incorrecta1="5",
                    respuesta_incorrecta2="6"
                ),
                Pregunta(
                    pregunta="¿Quién escribió 'Cien años de soledad'?",
                    respuesta_correcta="Gabriel García Márquez",
                    respuesta_incorrecta1="Mario Vargas Llosa",
                    respuesta_incorrecta2="Julio Cortázar"
                )
            ]

             # Agregar las preguntas a la base de datos
db.session.add_all(preguntas)
db.session.commit()