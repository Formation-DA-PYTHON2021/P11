from P11 import server
from P11.server import app

class TestDisplayBoard:
    client = app.test_client()

    def test_display_board(self):

        self.client.post(
             "/purchasePlaces",
            data={
                "places": 1,
                "club": server.clubs[2]["name"],
                "competition": server.competitions[0]["name"],
            }
        )

        result = self.client.get("/viewClubPoints")