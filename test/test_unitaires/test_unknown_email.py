from P11.server import app
from P11 import server


class TestLoginUnknownEmail:
    client = app.test_client()

    def test_valid_email(self):
        result = self.client.post("/showSummary",
                                  data={"email": server.clubs[0]['email']})
        print(server.clubs[0]['email'])
        assert result.status_code == 200

    def test_invalid_email(self):
        result = self.client.post("/showSummary",
                                  data={"email": "blabla@test.com"})
        assert result.status_code == 403

