import pytest
from app import app, CatBreed, get_index, create_cat
from flask import json, url_for

# From https://flask.palletsprojects.com/en/2.2.x/testing/
@pytest.fixture()
def client():
    app.config["WTF_CSRF_ENABLED"] = False
    app.config["SERVER_NAME"] = "test.local"
    client = app.test_client()

    CatBreed.drop_collection()

    # Pushing the app context allows us to make calls to the app like url_for
    # as if we were the running Flask app. Makes testing routes more resilient.
    ctx = app.app_context()
    ctx.push()

    yield client

    ctx.pop()


def test_index_through_client(client):
    response = client.get("/")
    assert response.status_code == 200
    d = json.loads(response.data)
    assert d == {}


def test_create_through_client(client):
    response = client.get(url_for("create_cat"))
    assert response.status_code == 201
    d = json.loads(response.data)
    assert d["style"] == "Sassy"

def test_index_returns_empty_dictionary():
    assert get_index() == {}

def test_can_retrieve_a_cat_that_is_saved(client):
    response = client.get(url_for("create_cat"))
    assert response.status_code == 201
    d = json.loads(response.data)
    assert d["style"] == "Sassy"
    # now retrieve the same cat
    response = client.get(url_for("get_cat", cat_id=d["id"]))
    d2 = json.loads(response.data)
    assert d2["style"] == d["style"]