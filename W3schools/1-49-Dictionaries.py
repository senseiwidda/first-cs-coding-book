thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
mydict={
    "name": "John",
    "age": 36,
    "country": "Norway"
}
print(mydict["country"])
print(mydict["name"])
mydict={
    "name": "John",
    "age": 36,
    "country": "Norway",
    "country": "Sweden"
}
print(mydict)
print(len(mydict))
notdict={
    "brand": "Ford",
    "electric": False,
    "year": 1964,  
    "colors": ["red", "white", "blue"]
}  
print(notdict)
print(type(notdict))
ashdict=dict(name="John", age=36, country="Norway")
print(ashdict)
