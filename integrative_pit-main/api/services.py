import requests


# ---------------------------
# COUNTRY API
# ---------------------------
def get_country_data(country):

    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()[0]

    currency_code = list(data.get("currencies", {}).keys())[0]
    currency_name = data.get("currencies", {}).get(currency_code, {}).get("name")

    return {
        "country": data.get("name", {}).get("common"),
        "capital": data.get("capital", [None])[0],
        "population": data.get("population"),
        "currency_code": currency_code,
        "currency_name": currency_name
    }


# ---------------------------
# CURRENCY API
# ---------------------------
def get_currency_rate(currency):

    url = "https://open.er-api.com/v6/latest/USD"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    rates = data.get("rates", {})

    return rates.get(currency)