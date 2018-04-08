import requests


def test_server_sends_200_response():
    """
    """
    response = requests.get('http://127.0.0.1:3000')
    assert response.status_code == 200
    assert response.text.startswith('<!DOCTYPE')


def test_server_sends_200_cowsay_response():
    """
    """
    response = requests.get('http://127.0.0.1:3000/cowsay')
    assert response.status_code == 200
    assert response.text.startswith('<!DOCTYPE')


def test_server_sends_200_cow_response():
    """
    """
    response = requests.get('http://127.0.0.1:3000/cow')
    assert response.status_code == 200
    assert 'You should speak up for yourself.' in response.text


def test_server_sends_404_response():
    """
    """
    response = requests.get('http://127.0.0.1:3000/monkey')
    assert response.status_code == 404
    assert response.text == 'Not Found'


def test_server_sends_cow_qs_back():
    """
    """
    msg = 'Hello world'
    response = requests.get(
        'http://127.0.0.1:3000/cow', params={'msg': msg})
    assert response.status_code == 200
    assert msg in response.text


def test_server_sends_cow_post_qs_back():
    """
    """
    msg = 'Hello world'
    response = requests.post('http://127.0.0.1:3000/cow', json={'msg': msg})
    assert response.status_code == 200
    assert msg in response.json()['content']
