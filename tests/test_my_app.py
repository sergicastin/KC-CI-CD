import pytest
from my_app import crear_tabla, agregar_practica, obtener_practicas, eliminar_practica

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
