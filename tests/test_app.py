# tests/test_app.py
import pytest
from toxicity_detector_app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_analyze_simulated(client):
    response = client.post('/analyze', json={"text": "You suck!"})
    assert response.status_code == 200
    assert 'label' in response.json[0]
