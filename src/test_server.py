import requests


def test_server_sends_200_response():
    """
    """
    response = requests.get('http://127.0.0.1:3000')
    assert response.status_code == 200
    assert response.text == 'You did a thing!'


def test_server_sends_404_response():
    """
    """
    response = requests.get('http://127.0.0.1:3000/monkey')
    assert response.status_code == 404
    assert response.text == 'Not Found'


def test_server_sends_qs_back():
    """
    """
    response = requests.get(
        'http://127.0.0.1:3000/test',
        params={'category': '"Hello world"'})
    assert response.status_code == 200
    assert response.text == 'we did the thing with the qs'
