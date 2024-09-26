from django.urls import reverse
from django.test import SimpleTestCase

class APIVersionURLTests(SimpleTestCase):
    def test_api_version_url(self):
        """Test that the API version URL resolves correctly."""
        url = reverse('api-version')
        self.assertEqual(url, '/api/version/')

    def test_api_version_url_uses_correct_view(self):
        """Test that the API version URL uses the correct view."""
        url = reverse('api-version')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_api_version_invalid_version(self):
        """Test the API version endpoint with an invalid version returns a 404."""
        url = reverse('api-version') + '?version=v100'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {"error": "Invalid version."})

    def test_api_version_without_version_param(self):
        """Test the API version endpoint without a version query param returns the default version."""
        url = reverse('api-version')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"version": "v1"})

    def test_api_version_with_supported_version(self):
        """Test the API version endpoint with a supported version."""
        url = reverse('api-version') + '?version=v2'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"version": "v2"})

    def test_api_version_with_empty_version_param(self):
        """Test the API version endpoint with an empty version parameter returns the default version."""
        url = reverse('api-version') + '?version='
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"version": "v1"})
