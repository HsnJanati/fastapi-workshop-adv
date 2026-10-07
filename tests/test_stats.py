"""Tests for the /stats endpoint."""

from fastapi.testclient import TestClient

from app.main import app
from app.store import profile_store

client = TestClient(app)

def test_stats(clean_store):
    profile_store["alice"] = {
        "username": "alice",
        "bio": "Developer",
        "age": 20
    }

    profile_store["bob"] = {
        "username": "bob",
        "bio": "Student",
        "age": 30
    }

    response = client.get("/stats")

    data = response.json()

    assert response.status_code == 200
    assert data["total_profiles"] == 2
    assert data["average_age"] == 25

def test_stats_empty_store(clean_store):
    response = client.get("/stats")
    
    data = response.json()
    
    assert response.status_code == 200
    assert data["total_profiles"] == 0
    assert data["average_age"] == 0


def test_stats_profile_without_age(clean_store):
    profile_store["alice"] = {
        "username": "alice",
        "bio": "Developer",
        "age": 20
    }

    profile_store["bob"] = {
        "username": "bob",
        "bio": "Student"
    }

    response = client.get("/stats")

    data = response.json()

    assert response.status_code == 200
    assert data["total_profiles"] == 2
    assert data["average_age"] == 20