# backend/tests/test_url_service.py

import pytest
import json


def test_retrieve_actual_url(test_app):
    response = test_app.post(
        "/", data=json.dumps({"actual_url": "https://www.google.com"})
    )

    assert response.status_code == 201

    encoded_url = response.json()["encoded_url"]

    response = test_app.get(f"/{encoded_url}/")

    assert response.status_code == 200
    assert response.json()["actual_url"] == "https://www.google.com"


def test_create_shorten_url(test_app):
    response = test_app.post(
        "/", data=json.dumps({"actual_url": "https://www.google.com"})
    )
    assert response.status_code == 201
    assert response.json()["encoded_url"] == "http://localhost:8000/1d5920f4"
