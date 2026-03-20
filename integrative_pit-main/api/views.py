from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import (
    CountryQuerySerializer,
    CountryCurrencyResponseV1,
    CountryCurrencyResponseV2
)

from .services import get_country_data, get_currency_rate


def home(request):
    return render(request,"home.html")


def v1_ui(request):
    return render(request,"v1.html")


def v2_ui(request):
    return render(request,"v2.html")

# -------------------------
# VERSION 1
# -------------------------
class CountryCurrencySummaryV1(APIView):

    @swagger_auto_schema(
        tags=["Country Currency API"],
        query_serializer=CountryQuerySerializer,
        responses={200: CountryCurrencyResponseV1}
    )
    def get(self, request):

        country = request.GET.get("country")

        if not country:
            return Response(
                {"error": "country parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        country_data = get_country_data(country)

        if not country_data:
            return Response(
                {"error": "Country not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        currency_code = country_data["currency_code"]

        rate = get_currency_rate(currency_code)

        if rate is None:
            return Response(
                {"error": "Currency API failed"},
                status=status.HTTP_502_BAD_GATEWAY
            )

        # DATA TRANSFORMATION
        result = {
            "country": country_data["country"],
            "capital": country_data["capital"],
            "currency": currency_code,
            "usd_to_currency_rate": rate,
            "converted_sample": round(rate * 10, 2)
        }

        return Response(result, status=status.HTTP_200_OK)


# -------------------------
# VERSION 2
# -------------------------
class CountryCurrencySummaryV2(APIView):

    @swagger_auto_schema(
        tags=["Country Currency API"],
        query_serializer=CountryQuerySerializer,
        responses={200: CountryCurrencyResponseV2}
    )
    def get(self, request):

        country = request.GET.get("country")

        if not country:
            return Response(
                {"error": "country parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        country_data = get_country_data(country)

        if not country_data:
            return Response(
                {"error": "Country not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        currency_code = country_data["currency_code"]

        rate = get_currency_rate(currency_code)

        if rate is None:
            return Response(
                {"error": "Currency API failed"},
                status=status.HTTP_502_BAD_GATEWAY
            )

        # IMPROVED STRUCTURE
        result = {

            "country_information": {
                "name": country_data["country"],
                "capital": country_data["capital"],
                "population": country_data["population"]
            },

            "currency_information": {
                "currency_code": currency_code,
                "currency_name": country_data["currency_name"],
                "usd_to_currency_rate": rate
            },

            "sample_conversion": {
                "1_usd": rate,
                "10_usd": round(rate * 10, 2),
                "50_usd": round(rate * 50, 2)
            }
        }

        return Response(result, status=status.HTTP_200_OK)