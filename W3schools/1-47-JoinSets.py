set1={"a","b","c"}
print(set1)
set2={1,2,3}
print(set2)
set3=set1.union(set2)   
print(set3)
set3=set1|set2
print(set3)
set4={"d","e","f"}
print(set4)
set5={"apple","banana","cherry"}
print(set5) 
thisset=set1.union(set2,set4,set5)
print(thisset)
myset=set1|set2|set4|set5
print(myset)
a={"x","y","z"}
b={7,8,9}
c=a.union(b)
print(c)
thisset.update(c)
print(thisset)
myset={"apple","banana","cherry"}
print(myset)
hisset={"google","microsoft","apple"}
print(hisset)
herset=myset.intersection(hisset)
print(herset)
herset=myset & hisset
print(herset)   
myset.intersection_update(hisset)
print(myset)
setA={"apple",1, "banana",0,"cherry"}
setB={False, "google", 1, "apple", 2, True}
setC=setA.intersection(setB)
print(setC)
setC=setA.difference(setB)
print(setC)
setC=setA - setB
print(setC)
myset.difference_update(hisset)
print(myset)