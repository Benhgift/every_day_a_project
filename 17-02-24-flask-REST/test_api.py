from requests import get


def test_api():
    response = get('http://localhost:5000').json()
    assert response['hello'] == 'world'
