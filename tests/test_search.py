"""Tests for the /search endpoint."""

from fastapi.testclient import TestClient

from app.main import app
from app.store import profile_store

client = TestClient(app)


def test_search_with_query():
    profile_store["alice"] = {"username": "alice", "bio": "dev"}
    profile_store["alex"] = {"username": "alex", "bio": "designer","age": 30}
    profile_store["bob"] = {"username": "ali", "bio": "manager", "age":45}

    response = client.get("/search?q=al&offset=0&limit=2&min_age=25&max_age=40")
    data = response.json()
    assert data["total"] == 1
    assert len(data["results"]) == 1


def test_search_empty_query():
    profile_store["carol"] = {"username": "carol", "bio": "tester"}
    response = client.get("/search?q=")
    data = response.json()
    assert data["total"] > 0
def test_search_pagination_limit(clean_store):
    profile_store["alice"] = {
        "username": "alice",
        "bio": "developer",
        "age": 20
    }

    profile_store["bob"] = {
        "username": "bob",
        "bio": "developer",
        "age": 25
    }

    profile_store["charlie"] = {
        "username": "charlie",
        "bio": "developer",
        "age": 30
    }

    response = client.get("/search?q=developer&offset=0&limit=2")
    data = response.json()

    assert response.status_code == 200
    assert data["total"] == 3
    assert len(data["results"]) == 2