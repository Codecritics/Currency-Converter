if __name__ == '__main__':

    conicoins_converter = {
        "RUB": 2.98,
        "ARS": 0.82,
        "HNL": 0.17,
        "AUD": 1.9622,
        "MAD": 0.208
    }

    coins = input()
    coins = float(coins)
    for currency, rate in conicoins_converter.items():
        print(f'I will get {round(coins * rate, 2)} {currency} from the sale of {coins} conicoins.')
