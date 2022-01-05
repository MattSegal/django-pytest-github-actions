from django.urls import reverse


def test_hello_view(client):
    url = reverse('hello')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'Hello world'
    

def test_goodbye_view(client):
    url = reverse('goodbye')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b'Goodbye world'
