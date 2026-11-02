"""Offline-Tests der API-Routen (kein Netz, keine Keys)."""

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture
def client(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    import main

    main.claims_db.clear()
    return TestClient(main.app), main


def test_starts_without_openai_key(client):
    http, _ = client
    assert http.get("/api/health").json() == {"status": "healthy"}


def test_latest_claim_not_shadowed_by_claim_id(client):
    http, main = client
    assert http.get("/api/claims/latest").json()["detail"] == "No claims found"
    main.claims_db["a"] = {"id": "a", "created_at": "2026-01-01"}
    main.claims_db["b"] = {"id": "b", "created_at": "2026-02-01"}
    assert http.get("/api/claims/latest").json()["id"] == "b"
    assert http.get("/api/claims/a").json()["id"] == "a"


def test_voice_needs_key_with_clear_error(client):
    _, main = client
    with pytest.raises(RuntimeError, match="OPENAI_API_KEY"):
        main.get_openai_client()
