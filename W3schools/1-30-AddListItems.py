thislist=["apple","banana","cherry"]
thislist.append("orange")  #Adding an item to the end of the list
print(thislist)
thislist.insert(1, "orange")  #Adding an item at the specified index
print(thislist)
tropiical=["mango","pineapple","papaya"]
thislist.extend(tropiical)  #Adding the elements of a list to another list
print(tropiical+thislist)
print(thislist)
thistuple=("kiwi","watermelon")
thislist.extend(thistuple)  #Adding the elements of a tuple to a list
print(thislist)