from P11 import server
from P11.server import app


class TestLoginUnknownEmail:
    client = app.test_client()

    def test_valid_email(self):
        result = self.client.post("/showSummary",
                                  data={"email": server.clubs[0]["email"]})
        data = result.data.decode()
        assert result.status_code == 200
        assert f"{server.clubs[0]['email']}" in data

    def test_invalid_email(self):
        result = self.client.post("/showSummary",
                                  data={"email": "blabla@test.com"})
        assert result.status_code == 403


