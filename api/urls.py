from django.urls import path
from .views import CountryCurrencySummaryV1, CountryCurrencySummaryV2

urlpatterns = [

    path(
        "api/v1/country-currency-summary/",
        CountryCurrencySummaryV1.as_view(),
        name="country-currency-summary-v1"
    ),

    path(
        "api/v2/country-currency-summary/",
        CountryCurrencySummaryV2.as_view(),
        name="country-currency-summary-v2"
    ),
]