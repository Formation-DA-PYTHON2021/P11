from P11 import server
from P11.server import app


class TestNoMoreTwelvePlacePerCompetition:

    client = app.test_client()

    def test_less_than_twelve(self):
        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": 6,
                "club": server.clubs[0]['name'],
                "competition": server.competitions[0]['name']
            }
        )
        assert result.status_code == 200

    def test_more_than_twelve_first(self):
        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": 13,
                "club": server.clubs[0]['name'],
                "competition": server.competitions[0]['name']
            }
        )
        assert result.status_code == 403

    def test_more_than_twelve_add(self):
        result = self.client.post(
            "/purchasePlaces",
            data={
                "places": 8,
                "club": server.clubs[0]['name'],
                "competition": server.competitions[0]['name']
            }
        )
        assert result.status_code == 403
