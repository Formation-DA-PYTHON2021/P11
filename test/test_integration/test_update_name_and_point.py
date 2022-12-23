from P11 import server
from P11.server import app


class TestUpdateNamePoint:
    client = app.test_client()

    def test_udapte_name_points(self):
        login = self.client.post(
            "/showSummary",
            data={"email": server.clubs[2]["email"]}
        )
        data = login.data.decode()

        assert login.status_code == 200
        assert f"<h2>Welcome, {server.clubs[2]['email']} </h2>" in data
