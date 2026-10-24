




prices=[400,500,600,700]
numbers=[5,77,88,21,90]
total=sum(prices)
length1=len(prices)
print(length1)
print(total)

t1=sum(numbers)
print(t1)

s='hello'

s1=s.upper()
print(s1)

l1=[54,36,78,99]
l1.append(100)
print(l1)


#input,parameter,argument
def intro(name,age):
    print('this is my intro and my name is',name ,"and age is", age)


intro('sunil',35)

def add_2_num(num1,num2,num3):
    o1=num1+num2+num3
    return o1

n1=add_2_num(30,40,66)
print(n1)

def add_all_numbers(numbers):
    total=0
    for i in numbers:
        total=total+i
    return total

n1=add_all_numbers(prices)
print(n1)