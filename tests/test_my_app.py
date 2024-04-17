import os
import pytest
from app import app, crear_tabla, agregar_practica, obtener_practicas, eliminar_practica

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
