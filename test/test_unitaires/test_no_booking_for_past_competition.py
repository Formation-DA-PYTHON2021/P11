from P11 import server
from P11.server import app


class TestNoBookingForPastCompetition:

    client = app.test_client()

    def test_book_present_competition(self, monkeypatch):
        date_test = '2023-12-01 15:00:00'
        monkeypatch.setitem(server.competitions[0], 'date', date_test)
        result = self.client.get(
            f"/book/{server.competitions[0]['name']}/{server.clubs[0]['name']}"
        )
        assert result.status_code == 200

    def test_book_past_competition(self):
        result = self.client.get(
            f"/book/{server.competitions[1]['name']}/{server.clubs[0]['name']}"
        )
        assert result.status_code == 403

