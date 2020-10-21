import requests

coindeskUrl = 'https://api.coindesk.com/v1/bpi/currentprice.json'
def main():
    dollars = convertToDollars()
    bitcoinRate = dollarToBitcoin(dollars)
    presentResults(dollars, bitcoinRate)

def converToDollars():
    while True:
        try:
            dollars = float(input('Enter dollar amount: '))
            if dollars >= 0:
                return dollars
            else:
                print('Please enter a value greater than 0. ')
        except ValueError:
            print('Error - Please enter a valid number')
def dollarsToBitcoin(dollars):
    exchangeRate = requestRate(dollars)
    bitcoin = convert(dollars, exchangeRate)
    return bitcoin
def requestRate(rate):
    try:
        response = requests.get(coindeskUrl)
        data = response.json()
        dollarsExchangeRate = data['bpi']['USD']['rateFloat']
    except Exception as e:
        print(f'Error occured. ', e)
def convert(dollars, bitcoinRate):
    return dollars * bitcoinRate
def presentResults(dollars, bitcoin):
    print(f'${dollars:.2f} equals a total of {bitcoin:.2f} bitcoins.')

if __name__ == '__main__':
    main()
