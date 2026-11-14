


f1=open('new.txt','r')
d=f1.read()
print(d)
f1.close()


with open('data1.txt','r') as f3:
    data=f3.read()
    print(data)

f2=open('data1.txt','w')
f2.write('hello world')
f2.close()

