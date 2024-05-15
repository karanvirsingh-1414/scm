# convert.py

def convert_currency(amount, from_currency, to_currency):
    # This is a simplified example; you would typically fetch real-time exchange rates here
    exchange_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.73},
        'EUR': {'USD': 1.18, 'GBP': 0.86},
        'GBP': {'USD': 1.38, 'EUR': 1.16},
        # Add more currency pairs as needed
    }

    if from_currency == to_currency:
        return amount

    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * rate
        return round(converted_amount, 2)

    return None

if __name__ == "__main__":
    # Example usage for testing
    amount = 100
    from_currency = "USD"
    to_currency = "EUR"
    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {result} {to_currency}")
