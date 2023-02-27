from flask import Flask


"""
Para ejecutar la app de Flask necesitamos un servidor web
que acepte las peticiones, las envíe a nuestro programa en Flask
y recoja los resultado para enviarlos al navegador.

Flask nos proporciona un servidor **solamente para desarrollo**
que nos facilita las pruebas en nuesto PC.

Para que esto funcione correctamente necesitamos dos variables de entorno:

- Linux/Mac
  export FLASK_APP=hello
  export FLASK_ENV=development (obsoleto)
  export FLASK_DEBUG=True

- Windows
  set FLASK_APP=hello
  set FLASK_ENV=development (obsoleto)
  set FLASK_DEBUG=True
"""

# instanciamos Flask y le pasamos un nombre para la app
app = Flask(__name__)


# mediante un decorador, asignamos una ruta (path) de la URL
# a la función que debe ejecutarse cuando se recibe una petición
# con esa ruta
@app.route('/')
def hola():
    return 'Hola, soy Flask. Y tú, ¿cómo te llamas?'


@app.route('/bye')
@app.route('/bye/con/varias/palabras')
def adios():
    return 'Adiós, te veo luego.'


@app.route('/new')
def nuevo():
    return 'Soy otra ruta nueva'
