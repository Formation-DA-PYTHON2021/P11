from P11 import server
from P11.server import app


class TestDisplayBoard:
    client = app.test_client()

    def test_display_board(self):
        club_points_before = int(server.clubs[2]['points'])
        places_booking = 10

        self.client.post(
            "/purchasePlaces",
            data={
                "places": places_booking,
                "club": server.clubs[2]["name"],
                "competition": server.competitions[0]["name"],
            }
        )

        result = self.client.get("/viewClubsPoints")
        data = result.data.decode()

        assert result.status_code == 200
        assert f"<td>{server.clubs[2]['name']}</td>" in data
        assert f"<td>{club_points_before - places_booking}</td>" in data
