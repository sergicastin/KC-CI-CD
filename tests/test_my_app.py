import os
import pytest
import sys
import json

# Obtener la ruta al directorio 'app' (un nivel hacia arriba desde la ubicación de este archivo)
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))

# Ruta al archivo JSON dentro de la carpeta app
secret_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app', 'secret.json'))

# Agregar el directorio 'app' al sys.path
sys.path.insert(0, app_path)

# Ahora puedes importar 'app.py' desde el directorio 'app'
from app import app, obtener_practicas

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
