from rest_framework import serializers


# Query Parameter Serializer
class CountryQuerySerializer(serializers.Serializer):
    country = serializers.CharField(
        help_text="Name of the country (example: Japan, Philippines)"
    )


# Response Serializer V1
class CountryCurrencyResponseV1(serializers.Serializer):
    country = serializers.CharField()
    capital = serializers.CharField()
    currency = serializers.CharField()
    usd_to_currency_rate = serializers.FloatField()
    converted_sample = serializers.FloatField()


# Response Serializer V2
class CountryInfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    capital = serializers.CharField()
    population = serializers.IntegerField()


class CurrencyInfoSerializer(serializers.Serializer):
    currency_code = serializers.CharField()
    currency_name = serializers.CharField()
    usd_to_currency_rate = serializers.FloatField()


class SampleConversionSerializer(serializers.Serializer):
    one_usd = serializers.FloatField()
    ten_usd = serializers.FloatField()
    fifty_usd = serializers.FloatField()


class CountryCurrencyResponseV2(serializers.Serializer):
    country_information = CountryInfoSerializer()
    currency_information = CurrencyInfoSerializer()
    sample_conversion = SampleConversionSerializer()