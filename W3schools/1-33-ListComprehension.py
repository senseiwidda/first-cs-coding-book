fruits=["apple","banana","cherry","kiwi","mango"]
print(fruits)
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)   
print(newlist)  

newlist=[x for x in fruits if "a" in x]
print(newlist)
newlist=[x for x in fruits if x!="apple"]
print(newlist)
if len(fruits)>2:
    newlist=[x for x in fruits]
newlist=[x for x in range(10)]
print(newlist)
newlist=[x for x in range(10) if x<5]
print(newlist)
newlist=[x.upper() for x in fruits]
print(newlist)
newlist=[x.lower() for x in fruits]
print(newlist)
newlist=[x if x!="banana" else "orange" for x in fruits]
if "orange" in newlist:
    newlist=['hello' for x in fruits]
print(newlist)