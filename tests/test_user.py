# pylint: disable=redefined-outer-name
"""Tests for users"""
import json
import jsend
import pytest
import configparser
from falcon import testing
import service.microservice
from urllib.parse import urlencode

@pytest.fixture()
def client():
    """ client fixture """
    return testing.TestClient(service.microservice.start_service())

def pytest_configure(config):
    pytest.user_id = None

def test_create_user(client):
    body = {
        'email': 'test@test.com',
        'is_admin': False
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = client.simulate_post('/users', json = body, headers = headers)
    assert response.status_code == 201

def test_get_user(client):
    response = client.simulate_get('/users')
    assert response.status_code == 200
    user = get_user_by_email(json.loads(response.content).get('data'), 'test@test.com')
    assert user is not None

    if user is not None:
        pytest.user_id = user.get("id")

def test_delete_user(client):
    assert pytest.user_id is not None
    if pytest.user_id is not None:
        resource_url = ''.join(['/users/', pytest.user_id])
        response = client.simulate_delete(resource_url)
        assert response.status_code == 200

def get_user_by_email(data, email):
    """A helper function to determine if a given email value is in the dataset
    and return the user associated to the email

    Parameters
    ----------
    data : list or dictionary
    email : string
    """

    if isinstance(data, list):
        for user in data:
            if user.get("email") == email:
                return user
    else:
        for key, val in data.items():
            if key == "email" and val == email:
                return data
    return None


