from forex_python.converter import CurrencyRates


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

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Invalid currency codes.")
        c = CurrencyRates()
        from_currency = from_currency
        to_currency = to_currency
        new_amt = c.convert(from_currency, to_currency, float(amount))
        return float("{:.4f}".format(new_amt))

    # Extraordinary functionality example:
    def list_supported_currencies(self):
        return list(self.exchange_rates.keys())
