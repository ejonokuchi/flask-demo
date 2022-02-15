from src import app


def test_get():
    app.testing = True
    client = app.test_client()

    r = client.get("/")
    assert r.status_code == 200
    assert "Success!" in r.data.decode("utf-8")


def test_post():
    app.testing = True
    client = app.test_client()

    r = client.post("/submit")
    assert r.status_code == 200
