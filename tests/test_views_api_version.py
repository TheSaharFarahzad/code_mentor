from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class APIVersionViewTests(APITestCase):
    def test_version_endpoint(self):
        """Test the version endpoint returns correct version."""
        url = reverse('api-version')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"version": "v1"})

    def test_version_with_path_versioning(self):
        """Test versioning with URLPathVersioning."""
        url = reverse('api-version')
        response = self.client.get(url + '?version=v2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"version": "v2"})

    def test_version_invalid(self):
        """Test the endpoint returns a 404 for an invalid version."""
        url = reverse('api-version')
        response = self.client.get(url + '?version=v100')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"error": "Invalid version."})

    def test_no_version_query_param(self):
        """Test the endpoint without version query param returns the default version."""
        url = reverse('api-version')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"version": "v1"})
