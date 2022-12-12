from locust import HttpUser, task, between

from P11.server import loadClubs, loadCompetitions


class ProjectPerfTest(HttpUser):
    wait_time: between(1, 5)

    def on_start(self):
        self.client.get("/")
        self.client.post("/showSummary", data={'email': loadClubs()[0]["email"]}, name="showSummary")

    @task
    def for_booking(self):
        self.client.get(
            f"/book/{loadCompetitions()[0]['name']}/{loadClubs()[0]['name']}",
            name="/book/..."
        )

    @task
    def after_booking(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "places": 0,
                "club": loadClubs()[0]['name'],
                "competition": loadCompetitions()[0]['name']
            },
            name="/purchasePlaces"
        )

