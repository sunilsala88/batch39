

# number=121
# while True:

#     print(number)
#     number=number+1
#     if number>=130:
#         break

# print('----')

# number=121
# while number<130:
#     print(number)
#     number=number+1



prices=[300,400,7500,6000,7000]

for i in range(len(prices)):
    print(i,prices[i])

print('------')

i=0
while True:

    if i==5:
        break
    print(i,prices[i])
    i=i+1
print('----')
i=0
while i<len(prices):
    print(i,prices[i])
    i=i+1

#higest number in a list
#n fib number

i=0
max1=0
while True:
    if i>=len(prices):
        break
    
    if prices[i]>max1:
        max1=prices[i]
    i=i+1
print(max1)


fib=[0,1]
fib_count=10

while True:

    if fib_count==2:
        break
    # print(fib_count)
    prev=fib[-1]
    prev_prev=fib[-2]
    current=prev+prev_prev
    fib.append(current)
    fib_count=fib_count-1

print(fib)
print('----')
fib=[0,1]
count=2
fib_count=10
while True:

    if count==fib_count:
        break
    # print(count)
    prev=fib[-1]
    prev_prev=fib[-2]
    current=prev+prev_prev
    fib.append(current)
    count=count+1
print(fib)