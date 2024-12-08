import requests

def test_php_backend():
    # URL del servidor PHP (ajusta el puerto si es necesario)
    url = "http://localhost:8080"
    
    # Realiza una solicitud GET al servidor
    response = requests.get(url)

    # Verifica que el estado de la respuesta sea 200 (OK)
    assert response.status_code == 200
    
    # Verifica que la respuesta contenga el texto esperado
    assert "Hola desde el Backend PHP!" in response.text