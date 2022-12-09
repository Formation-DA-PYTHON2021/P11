from locust import HttpUser, task, between

from P11.server import loadClubs


class ProjectPerfTest(HttpUser):
    wait_time: between(1, 5)

    def on_start(self):
        self.client.get("/")
        self.client.post("/showSummary", data={'email': loadClubs()[0]["email"]})

    @task
    def task1(self):
        pass
