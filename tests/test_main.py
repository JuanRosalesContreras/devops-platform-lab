from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_default(monkeypatch):
    monkeypatch.delenv("APP_ENV", raising=False)

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "application": "devops-platform-lab",
        "environment": "local",
        "status": "running",
    }


def test_root_custom_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV", "dev")

    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["environment"] == "dev"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
    }


def test_version_default(monkeypatch):
    monkeypatch.delenv("APP_VERSION", raising=False)

    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {
        "version": "1.0.0",
    }


def test_version_custom(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.1.0")

    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {
        "version": "1.1.0",
    }


def test_feature_disabled_by_default(monkeypatch):
    monkeypatch.delenv("FEATURE_FLAG", raising=False)

    response = client.get("/feature")

    assert response.status_code == 200
    assert response.json() == {
        "feature_enabled": False,
    }


def test_feature_enabled(monkeypatch):
    monkeypatch.setenv("FEATURE_FLAG", "true")

    response = client.get("/feature")

    assert response.status_code == 200
    assert response.json() == {
        "feature_enabled": True,
    }
