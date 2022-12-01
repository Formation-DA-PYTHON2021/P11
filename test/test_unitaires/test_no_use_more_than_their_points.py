from P11 import server
from P11.server import app

class TestNoUseMoreThanTheirPoints:

    client = app.test_client()
    competition = [
        {
            "name": "Test_points competition",
            "date": "2022-12-01 15:00:00",
            "numberOfPlace": "25"
        }
    ]

    club = [
        {
            "name": "Test_points club",
            "email": "test@test.com",
            "points": "10"
        }
    ]

    def setup_method(self):
        server.competitions = self.competition
        server.clubs = self.club

    def test_points_allowed(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "place": 5,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"],
            }
        )
        assert int(self.club[0]["points"]) >= 0

    def test_more_points_than_allowed(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "place": 50,
                "club": self.club[0]["name"],
                "competition": self.competition[0]["name"],
            }
        )
        assert int(self.club[0]["points"]) >= 0
