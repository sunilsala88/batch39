
try:
    num1=int(input('Enter first number:'))
    num2=int(input('Enter second number:'))
    print(num1/num2)
except Exception as e:
    print('Error occured')
    print(e)

print('closing position')