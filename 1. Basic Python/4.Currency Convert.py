from currency_converter import CurrencyConverter

c = CurrencyConverter()
amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ").upper()
to_currency = input("To currency (e.g., KRW): ").upper()

result = c.convert(amount, from_currency, to_currency)
print(f"{amount} {from_currency} = {result:.2f} {to_currency}")