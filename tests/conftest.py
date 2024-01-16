import pytest
from flask import Flask

from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        dict(
            TESTING=True,
        ),
    )
    return app


@pytest.fixture()
def client(app: Flask):
    return app.test_client()


@pytest.fixture()
def runner(app: Flask):
    return app.test_cli_runner()
