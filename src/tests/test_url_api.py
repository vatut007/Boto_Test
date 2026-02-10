from http import HTTPStatus
from schemas.urlmap import UrlMapRead


def test_create_shorten_success(client):
    """Тест: успешное создание короткой ссылки."""
    response = client.post(
        "/shorten",
        json={"url": "https://example.com/very/long/path"}
    )
    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert "short_link" in data

    UrlMapRead.model_validate(data)


def test_redirect_success(client):
    """Тест: успешный редирект по короткому коду."""
    response = client.post(
        "/shorten",
        json={"url": "https://example.com/target"}
    )
    data = response.json()
    response = client.get(data['short_link'])
    assert response.history[0].status_code == HTTPStatus.TEMPORARY_REDIRECT
    assert response.history[0].headers["location"] == "https://example.com/target"


def test_redirect_not_found(client):
    """Тест: 404 при отсутствии короткой ссылки."""
    response = client.get("/nonexistent")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["detail"] == "Ссылка не найдена"


def test_redirect_empty_code(client):
    """Тест: 404 при пустом коде."""
    response = client.get("/")
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_create_shorten_invalid_url(client):
    """Тест: ошибка при передаче некорректного URL."""
    response = client.post("/shorten", json={"url": "not-a-url"})
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert "detail" in response.json()
