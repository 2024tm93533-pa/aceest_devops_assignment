import pytest
import json
from app import create_app
from app.models import db, Client

@pytest.fixture
def client(tmp_path):
    db_path = tmp_path / "test.db"
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['TESTING'] = True
    with app.app_context():
        db.init_app(app)
        db.create_all()
        yield app.test_client()

def test_client_crud(client):
    # create
    rv = client.post("/clients/", json={"name": "Test User", "age": 30})
    assert rv.status_code == 201
    data = rv.get_json()
    assert data["name"] == "Test User"

    client_id = data["id"]

    # get
    rv = client.get(f"/clients/{client_id}")
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["id"] == client_id

    # update
    rv = client.put(f"/clients/{client_id}", json={"age": 31})
    assert rv.status_code == 200
    data = rv.get_json()
    assert data["age"] == 31

    # list
    rv = client.get("/clients/")
    assert rv.status_code == 200
    data = rv.get_json()
    assert isinstance(data, list) and any(c["id"] == client_id for c in data)

    # delete
    rv = client.delete(f"/clients/{client_id}")
    assert rv.status_code == 200