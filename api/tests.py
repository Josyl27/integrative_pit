from django.test import TestCase
from rest_framework.test import APIClient


class CountryCurrencyTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_country_currency_summary_v1(self):

        response = self.client.get(
            "/api/v1/country-currency-summary/?country=Japan"
        )

        self.assertEqual(response.status_code, 200)


    def test_country_currency_summary_v2(self):

        response = self.client.get(
            "/api/v2/country-currency-summary/?country=Japan"
        )

        self.assertEqual(response.status_code, 200)