from flask.testing import FlaskClient


class TestAuth:
    def test(self, client: FlaskClient):
        ...

    def test_403_unauthenticated(self, client: FlaskClient):
        ...
