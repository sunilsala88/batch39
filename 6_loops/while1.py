


number=1
while True:
    if number==10:
        break
    print(number)
    number=number+1

#all even numbers from 1 to 100

even=[]
number=1
while True:
    if len(even)>100:
        break
    if number%2==0:
        even.append(number)
    number=number+1
print(even)



list1=[11,33,55,22,13]
#0,1,2,3,4
print('------')
i=0
while True:
    if i>4:
        break
    print(i,list1[i])
    i=i+1
    
print('------')
for i in range(5):
    print(i,list1[i])