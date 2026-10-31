



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

# p=get_porfolio(stock_prices)
# print(p)





def fun1(x,y): #2,3
    print(greet)
    o=x**2 +y #4+3=7
    return o


def fun2(a,b):
    i=fun1(a,b) #7
    return i+b**2#7+9

def fun3(x,y):
    a1=fun1(x,y) #7
    a2=fun2(x,y) #16
    return a1+a2#16+7


# output=fun3(2,3)
# print(output)
greet='hello'

#local and global
print(greet)

#calculatar

def start_calculator():

    while True:


        operation=input('enter the operation symbol (press q to exit)')

        if operation.lower()=='q':
            print('exiting the code')
            break


        num1=int(input(' enter num 1'))
        num2=int(input(' enter num 2'))

        if operation=='+':
            result=num1+num2
        if operation=='-':
            result=num1-num2
        if operation=='*':
            result=num1*num2
        if operation=='/':
            result=num1/num2
        print(result)


start_calculator()