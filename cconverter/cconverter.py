def get_coins() -> int:
    return int(input("Please, enter the number of conicoins you have:"))


def get_rate_exchange() -> int or float:
    rate_ = input("Please, enter the exchange rate:")
    try:
        result = int(rate_)
    except ValueError:
        result = float(rate_)

    return result


def print_the_value_dollars(dollars) -> None:
    print("The total amount of dollars:", dollars)


if __name__ == '__main__':
    coins = get_coins()
    rate = get_rate_exchange()
    print_the_value_dollars(coins * rate)
