#type 1 loop
stock_name=['tsla','goog','msft']
for i in stock_name:
    print(i)

prices=[333,444,555,666]
total=0
for i in prices:
    total=total+i
print(total)
print(len(prices))
print(sum(prices))

#type2 
print(list(range(101,200)))
for i in range(10):
    print('hello world')

even=[]
for i in range(101):
    if i%2==0:
        even.append(i)
print(even)

#type 3
sectors=['tech','bank','fmcg','oil']

for i in range(4):
    print(sectors[i])

prices=[2,3,4,5]
volumes=[30,40,50,60]
#vwap
num=0
den=0
for i in range(4):
    p1=prices[i]
    v1=volumes[i]
    print(p1,v1)
    num=num+p1*v1
    den=den+v1
print(num,den)
print(num/den)

list1=[23,56,89,45,25]
print(max(list1))
large=list1[0]
for i in list1:
    if i>large:
        large=i

print(large)

print(list1.sort())
print(list1)


list1=[23,56,89,45,25]
sort_list=[]
for i in range(5):
    small=list1[0]
    for i in list1:
        if i<small:
            small=i
    sort_list.append(small)
    list1.remove(small)
print(sort_list)


l1=[33,55,66,55,44,55,22,55,11]
number=55
count=0
for i in l1:
    if number==i:
        count=count+1

print(count)


fib=[0,1]
number=15
for i in range(number-2):
    last=fib[-1]
    last2=fib[-2]
    current=last+last2
    fib.append(current)
print(fib)