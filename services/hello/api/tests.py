from rest_framework.test import APITestCase


class HealthTests(APITestCase):
    def test_health_ok(self):
        r = self.client.get("/health/")
        assert r.status_code == 200
        assert r.json()["status"] == "ok"
