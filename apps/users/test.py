from rest_framework.test import APITestCase, APIClient
from base64 import b64encode

from .models import User


class AdminTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="admin2@example.com",
            password="12345",
            first_name="Alex",
            is_superuser=True,
            is_staff=True
        )

    def test_basic_auth(self):
        client = APIClient()

        credentials = b64encode(b"admin2@example.com:12345").decode("utf-8")
        response = client.get(
            "/api/v1/auth/users/",
            HTTP_AUTHORIZATION="Basic " + credentials
        )

        print("Response:", response.status_code, response.json() if response.status_code == 200 else response.content)
        self.assertEqual(response.status_code, 200)
