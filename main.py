
def main():
    while True:
        currency = input('Enter currency name (USD or EUR): ')
        if currency not in ('USD', 'EUR'):
            print('Incorrect input')
            continue

if __name__ == '__main__':
    main()