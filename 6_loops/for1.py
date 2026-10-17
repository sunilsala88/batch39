

l1=[22,33,44,55,66]

#type 1
total=1
for num in l1:
    total=total+num

print(total)
average=total/len(l1)

print(average)

#type 2

print(list(range(205,210)))

#str(),int(),float(),list()

print(list('hello'))

for i in range(10):
   print('hello world')


final=[]
count=0
for i in range(3):
    temp_list=[]
    for i in range(10):
        temp_list.append(count)
        count=count+1
    final.append(temp_list)
print(final)



s1='tsla-goog-amzn-nifty50'
print(s1.split(','))