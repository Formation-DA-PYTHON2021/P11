from P11 import server
from P11.server import app

class TestLoginLogout :
    client = app.test_client()

    def test_login_logout(self):
        login = self.client.post(
            "/showSummary",
            data={"email": server.clubs[0]["email"]}
        )
        logout = self.client.get("/logout")
        assert login.status_code == 200
        assert logout.status_code == 302


