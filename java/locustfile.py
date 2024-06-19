from locust import HttpUser, task


class JavaFunctionTest(HttpUser):

    @task
    def hello(self):
        self.client.get("/api/AzureWebAdapter/hello")

    @task
    def create_content(self):
        self.client.post("/api/AzureWebAdapter/content",
                         json={"color": "#00ff00", "title": "green"})

    @task
    def read_content(self):
        self.client.get("/api/AzureWebAdapter/content?id=1")

    @task
    def update_content(self):
        self.client.post("/api/AzureWebAdapter/content/update?id=4",
                        json={"color": "#ff0000", "title": "red"})
