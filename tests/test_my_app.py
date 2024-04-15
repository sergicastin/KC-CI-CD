import os
import sys
import pytest

# Agregar el directorio 'app' al PYTHONPATH
current_dir = os.path.dirname(os.path.realpath(__file__))
app_dir = os.path.join(current_dir, '..', 'app')
sys.path.append(app_dir)

# Importar funciones desde app.py
from ..app import crear_tabla, agregar_practica, obtener_practicas, eliminar_practica


@pytest.fixture
def db_connection():
    connection = None
    return connection

def test_crear_tabla(db_connection):
    crear_tabla()

def test_agregar_practica(db_connection):
    agregar_practica("Test Práctica", "test@example.com", "Test", "http://example.com")

def test_obtener_practicas(db_connection):
    practicas = obtener_practicas()

def test_eliminar_practica(db_connection):
    eliminar_practica(1)
