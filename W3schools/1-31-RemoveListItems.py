thislist=["apple","banana","cherry"]
print(thislist)
thislist.remove("banana")  #Removing an item by specifying its name
print(thislist)
morefruits=["orange","kiwi","grape"]
thislist.extend(morefruits)  #Removing the last item
print(thislist)
thislist.remove(morefruits[1])  #Removing the specified item from the list
print(thislist)
mylist=["apple","banana","cherry"]
mylist.pop(1)#Removing the last item of the list
print(mylist)
mylist.pop()
print(mylist)
hislist=["apple","banana","cherry"]
print(hislist)
del hislist[0]  #Removing an item at the specified index
print(hislist)
del hislist  #Deleting the entire list
mylist.clear()
print(mylist)  #Clearing the list
