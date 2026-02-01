thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
a=thisdict["model"]
print(a)
b=thisdict.get("model")
print(b)
c=thisdict.get("year")
print(c)
d=thisdict.keys()
print(d) 
print(thisdict)
car={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
e=car.keys()
print(e)
car["color"]="red"
print(e)
f=thisdict.values()
g=car.values()
print(f)
car["year"]=2020
print(g)
