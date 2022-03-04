from json import loads

from requests import get

if __name__ == '__main__':

    while True:
        try:
            currency_code = input()
            message = "Your input is does not look like a currency Code. Please try again:"
            assert (len(currency_code) == 3 and currency_code.isupper()), message
        except Exception as err:
            print(err)
        else:
            break
    URL = f'http://www.floatrates.com/daily/{currency_code}.json'
    conversion_code = loads(get(URL).text)

    print(conversion_code['usd'], conversion_code['eur'], sep="\n")
