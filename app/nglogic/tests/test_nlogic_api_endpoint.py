from rest_framework import status
from rest_framework.test import APITestCase

from conftest import DEFAULT_API_URL_BASE


class ProductViewTests(APITestCase):
    def test_get_index_from_endpoint(self):
        response = self.client.get(f"{DEFAULT_API_URL_BASE}/18/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("idx", response.data)  # noqa

        assert response.data["idx"] == 0  # noqa
