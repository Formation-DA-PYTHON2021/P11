from P11 import server
from P11.server import app


class TestUpdatePoint:

    client = app.test_client()

    def test_update_point(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "places": 1,
                "club": server.clubs[1]["name"],
                "competition": server.competitions[0]["name"],
            }
        )
        assert server.clubs[1]['points'] == 3