from collections import defaultdict
from json import loads

from requests import get


def input_currency_code() -> str:
    exception_currency_code_msg = "Your input is does not look like a currency Code. Please try again:"
    while True:
        try:
            currency_code = input()
            assert (
                               len(currency_code) == 3 and currency_code.islower()) or currency_code == "", exception_currency_code_msg
        except Exception as err:
            print(err)
        else:
            break
    return currency_code


if __name__ == '__main__':
    currency_to_change = input_currency_code()
    currencies_cached = defaultdict(int)
    for currency in ('eur', 'usd'):
        if currency_to_change != currency:
            conversion_code_dict = loads(get(f'http://www.floatrates.com/daily/{currency_to_change}.json').text)
            currencies_cached[currency] = conversion_code_dict[currency]['rate']

    while True:
        wanted_currency = input_currency_code()
        if wanted_currency:
            cash_of_currency_to_change = int(input())
            print("Checking the cache...")
            if wanted_currency in currencies_cached:
                print("Oh! It is in the cache!")
                converted_value = cash_of_currency_to_change * currencies_cached[wanted_currency]
                print(f'You received {round(converted_value, 2)} {wanted_currency.upper()}.')
            else:
                print("Sorry, but it is not in the cache!")
                URL = f'http://www.floatrates.com/daily/{currency_to_change}.json'
                conversion_code_dict = loads(get(URL).text)
                currencies_cached[wanted_currency] = conversion_code_dict[wanted_currency]['rate']
                converted_value = cash_of_currency_to_change * currencies_cached[wanted_currency]
                print(f"You received {round(converted_value, 2)} {wanted_currency.upper()}.")
        else:
            break
