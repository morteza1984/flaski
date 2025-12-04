import pytest
from app import app, my_sum


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """Testet, ob die Home-Route funktioniert"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Hello CI/CD" in rv.data

