thislist=["apple","banana","cherry"]
print(thislist)
thislist[1]="blackcurrant"  #Changing the second item
print(thislist)
mylist=["apple","banana","cherry","orange","kiwi","mango"]
mylist[1:3]=["blackcurrant","watermelon"]  #Changing items from index 1 to 2
print(mylist)
hislist=["apple","banana","cherry"]
print(hislist)
hislist[1:2]["blackcurrant","watermelon"]  #Changing every second item
print(hislist)
herlist=["apple","banana","cherry","orange","kiwi","mango"]
print(herlist)
herlist[1:3]=["watermelon"]  #Changing items from index 1 to 2 with one item
print(herlist)
herlist.insert(2, "watermelon")
print(herlist)
