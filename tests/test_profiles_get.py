"""Tests for the /profiles  endpoints."""

from fastapi.testclient import TestClient

from app.main import app
from app.store import profile_store
client = TestClient(app)


def test_get_profiles(clean_store):
    profile_store["alice"] = {
    "username": "alice",
    "bio": "Developer",
    "age": 22
    }

    profile_store["bob"] = {
    "username": "bob",
    "bio": "Student",
    "age": 25
    }
    test_data = [
    {"username": "alice", "bio": "Developer", "age": 22},
    {"username": "bob", "bio": "Student", "age": 25}
    ]
    response = client.get("/profiles")
    assert response.status_code == 200
    assert response.json() == test_data

def test_get_zero_profiles(clean_store) : 
    response = client.get("/profiles")
    dt = []
    assert response.status_code == 200
    assert response.json() == dt