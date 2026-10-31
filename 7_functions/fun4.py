



stock_prices={'tsla':300,'amzn':900,'goog':980,'nifty':799}

def get_porfolio(stock_prices):
    portfolio=[]

    while True:
        
        name=input('enter the stock name(press q to exit)')
        print(name)

        if name.upper()=='Q':
            break

        price=stock_prices.get(name)
        if price is  None:
            print('this name is invalid try again' )
        else:
            portfolio.append(name)

    return (portfolio)

p=get_porfolio(stock_prices)
print(p)