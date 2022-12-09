from P11.server import app
from P11 import server

class TestLoginUnknownEmail:
    client = app.test_client()

    club = [
        {
            "name": "Test_place_club",
            "email": "test@test.com",
            "points": "25"
        }
    ]

    def setup_method(self):
        server.clubs = self.club

    def test_valid_email(self):
        result = self.client.post("/showSummary",
                                  data={"email": "test@test.com"})
        assert result.status_code == 200

    def test_invalid_email(self):
        result = self.client.post("/showSummary",
                                  data={"email": "blabla@test.com"})
        assert result.status_code == 403


