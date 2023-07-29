from currency_converter import CurrencyConverter

def main():
    converter = CurrencyConverter()

    print("Welcome to Currency Converter!")
    print("Supported currencies:", converter.list_supported_currencies())

    amount = 100  # Replace this with your desired amount
    from_currency = "USD"  # Replace this with your desired source currency code
    to_currency = "EUR"    # Replace this with your desired target currency code

    result = converter.convert(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()
