import os
import pytest
import sys
import json

# Obtener la ruta al directorio 'app' (un nivel hacia arriba desde la ubicación de este archivo)
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))

# Agregar el directorio 'app' al sys.path
sys.path.insert(0, app_path)

# Ahora puedes importar 'app.py' desde el directorio 'app'
from app import app, crear_tabla, agregar_practica, obtener_practicas, eliminar_practica

# Obtener la ruta completa al archivo 'secret.json' dentro del directorio 'app'
secret_path = os.path.abspath(os.path.join(app_path, 'secret.json'))

print("Ruta esperada para secret.json:", secret_path)

# Cargar las variables de entorno desde el archivo JSON
with open(secret_path) as secret_file:
    config = json.load(secret_file)
    for key, value in config.items():
        os.environ[key] = value

@pytest.fixture
def client():
    # Configurar la aplicación en modo de prueba
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_index(client):
    # Realizar una solicitud GET a la ruta '/'
    response = client.get('/')

    # Verificar que la respuesta sea exitosa (código 200)
    assert response.status_code == 200

def test_agregar_practica(client):
    # Realizar una solicitud POST a la ruta '/agregar' con datos de práctica válidos
    response = client.post('/agregar', data={'nombre': 'Test Práctica', 'correo': 'test@example.com', 'categoria': 'Test', 'link': 'http://example.com'})

    # Verificar que la redirección fue exitosa (código 302)
    assert response.status_code == 302

    # Verificar que la práctica fue agregada correctamente
    practicas = obtener_practicas()
    assert len(practicas) == 1
    assert practicas[0]['nombre'] == 'Test Práctica'

def test_eliminar_practica(client):
    # Agregar una práctica para luego eliminarla
    agregar_practica('Prueba', 'prueba@example.com', 'Prueba', 'http://prueba.com')

    # Obtener la práctica recién agregada
    practicas = obtener_practicas()
    assert len(practicas) == 1
    practica_id = practicas[0]['id']

    # Realizar una solicitud POST para eliminar la práctica
    response = client.post(f'/eliminar/{practica_id}')

    # Verificar que la redirección fue exitosa (código 302)
    assert response.status_code == 302

    # Verificar que la práctica fue eliminada correctamente
    practicas = obtener_practicas()
    assert len(practicas) == 0
