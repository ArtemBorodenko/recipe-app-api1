from django.urls import reverse


class TestHealthCheck:
    url = reverse('health-check')

    def test_health_check(self, client):
        response = client.get(TestHealthCheck.url)
        assert response.status_code == 200, 'Health Check failed'