from P11.server import app


class TestLoginUnknownEmail:
    client = app.test_client()

    def test_valid_email(self):
        result = self.client.post("/showSummary",
                                  data=dict(email="admin@irontemple.com"))
        assert result.status_code == 200

    def test_invalid_email(self):
        result = self.client.post("/showSummary",
                                  data={"email": "blabla@test.com"})
        assert result.status_code == 403


