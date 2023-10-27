from test_conf import client


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


def test_read_teapot():
    response = client.get("/teapot")
    assert response.status_code == 418


def test_read_docs():
    response = client.get("/docs")
    assert response.status_code == 200


def test_read_redoc():
    response = client.get("/redoc")
    assert response.status_code == 200
