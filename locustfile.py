from locust import HttpUser, task, constant


class WebsiteUser(HttpUser):
    wait_time = constant(3)
    host = "http://pycemaker.herokuapp.com"

    def on_start(self):
        response = self.client.post("/registrar", json={
            "name": "Roberto Campos",
            "email": "robertocampos@email.com",
            "password": "1234",
            "cellphoneNumber": "12999998888"
        })
        response = response.json()
        self.client.delete("/usuario/delete/%s" % response["id"])

    @task
    def usuarios(self):
        self.client.get("/usuarios")
