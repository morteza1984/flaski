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


def test_sum():
    result = my_sum(5, 5)
    assert result == 10
    assert my_sum(-5, 5) == 0
    assert my_sum(0, 0) == 0
