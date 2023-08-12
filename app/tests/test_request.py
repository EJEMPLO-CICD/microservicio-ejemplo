import pytest

from loguru import logger

from app.main import app

from fastapi.testclient import TestClient

from app.config.environment import get_environment_variables

env = get_environment_variables()

client = TestClient(app)

def test_microservice_up():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "this is microservice ONE"}
    logger.info(response.json())

def test_inference_up():
    response = client.get(env.HOST_MODEL_ADMISSION)
    assert response.status_code != 500
    print(response.json())
