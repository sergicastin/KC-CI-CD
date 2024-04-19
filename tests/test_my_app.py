import os
import sys
import json
import pytest

# Obtener la ruta al directorio 'app' (un nivel hacia arriba desde la ubicación de este archivo)
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))

secret_path = os.path.join(os.path.dirname(__file__), 'secret.json')
with open(secret_path) as secret_file:
    # Cargar las variables secretas desde el archivo JSON
    config = json.load(secret_file)

# Agregar el directorio 'app' al sys.path
sys.path.insert(0, app_path)

# Ahora puedes importar 'app.py' desde el directorio 'app'
from app import agregar_practica, obtener_practicas, eliminar_practica

@pytest.fixture
def db_connection():
    connection = None
    return connection

def test_agregar_practica(db_connection):
    agregar_practica("Test Práctica", "test@example.com", "Test", "http://example.com")

def test_obtener_practicas(db_connection):
    practicas = obtener_practicas()

def test_eliminar_practica(db_connection):
    # Primero, agregamos una práctica para luego eliminarla
    agregar_practica("Test Práctica", "test@example.com", "Test", "http://example.com")
    # Obtenemos la práctica recién agregada para obtener su ID
    practicas = obtener_practicas()
    # Suponemos que la primera práctica en la lista es la que acabamos de agregar
    if practicas:
        practica_id = practicas[0]['id']
        eliminar_practica(practica_id)
