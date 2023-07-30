import requests

api_key = "cf2245abad6e7e3e58271810"
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"


class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = self.get_exchange_rates()

    def get_exchange_rates(self):
        return {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.72,
            # Add more currencies and their rates as needed.
        }

    @staticmethod
    def convert(amount, from_currency, to_currency):
        complete_url = url + from_currency
        response = requests.get(complete_url)
        data = response.json()

        if data['result'] == 'error':
            return "Error: " + data['error-type']

        rate = data['conversion_rates'][to_currency]
        return float("{:.4f}".format(amount * rate))

    # Extraordinary functionality example:
    def list_supported_currencies(self):
        return list(self.exchange_rates.keys())
