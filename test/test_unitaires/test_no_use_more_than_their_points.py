from P11 import server
from P11.server import app

class TestNoUseMoreThanTheirPoints:

    client = app.test_client()

    def test_points_allowed(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "places": 5,
                "club": server.clubs[0]["name"],
                "competition": server.competitions[0]["name"],
            }
        )
        assert int(server.clubs[0]["points"]) >= 0

    def test_more_points_than_allowed(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "places": 50,
                "club": server.clubs[0]["name"],
                "competition": server.competitions[0]["name"],
            }
        )
        assert server.clubs[0]["points"] >= 0
