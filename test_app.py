import pytest
from app import app

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_square():
    client = app.test_client()
    response = client.get('/square/4')
    assert response.status_code == 200
    assert b"16" in response.data
