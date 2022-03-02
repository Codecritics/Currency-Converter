if __name__ == '__main__':
    conicoins = int(input())

    converter = dict(conicoins=100)
    print(f'I have {conicoins} conicoins.')
    print(f'{conicoins} conicoins cost {conicoins * converter["conicoins"]} dollars.')
    print('I am rich! Yippee!')
