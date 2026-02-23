thislist=["apple","banana","cherry"]
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])  
i=0
while i < len(thislist):
    print(thislist[i])
    i=i+1
mylist=["banana","apple","cherry"]
[print(x) for x in mylist]
for i in range(len(mylist)):
    if len(mylist[i])>5:
        print(mylist[i])