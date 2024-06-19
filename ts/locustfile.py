from locust import HttpUser, task


class GoFunctionTest(HttpUser):

    @task
    def hello(self):
        self.client.get("/api/hello")

    @task
    def create_content(self):
        self.client.post("/api/content",
                         json={"color": "#0000ff", "title": "blue"})


    @task
    def read_content(self):
        self.client.get("/api/content?id=1")

    @task
    def update_content(self):
        self.client.put("/api/content?id=4",
                        json={"color": "#ff0000", "title": "red"})
