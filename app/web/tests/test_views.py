import pytest
from django.urls import reverse

from web.models import PageViewCount


def test_goodbye_view(client):
    url = reverse("goodbye")
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b"Goodbye world"


@pytest.mark.django_db
def test_hello_view(client):
    url = reverse("hello")
    assert PageViewCount.objects.count() == 0
    response = client.get(url)

    assert response.status_code == 200
    assert PageViewCount.objects.count() == 1
    counter = PageViewCount.objects.last()
    assert counter.count == 1
    assert b"Hello world" in response.content
    assert b"The counter is: 1" in response.content

    response = client.get(url)
    assert response.status_code == 200
    counter.refresh_from_db()
    assert counter.count == 2
    assert b"The counter is: 2" in response.content
