from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_get_employees():
    client = app.test_client()

    response = client.get("/employees")

    assert response.status_code == 200
    assert len(response.json) == 3


def test_get_employee():
    client = app.test_client()

    response = client.get("/employees/1")

    assert response.status_code == 200
    assert response.json["name"] == "Anas Qureshi"


def test_employee_not_found():
    client = app.test_client()

    response = client.get("/employees/100")

    assert response.status_code == 404