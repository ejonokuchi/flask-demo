from src import app


def test_home():
    app.testing = True
    client = app.test_client()

    r = client.get("/")
    assert r.status_code == 200
