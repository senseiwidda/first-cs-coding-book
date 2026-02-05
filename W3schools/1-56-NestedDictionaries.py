print("hi")
myfamily ={
    "child1": {
        "name": "Emil",
        "year": 2004
    },              
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    },
}
print(myfamily)
child1 ={
    "name": "Emil",
    "year": 2004
}
child2={
    "name": "Tobias",
    "year": 2007
}
child3={
    "name": "Linus",
    "year": 2011    
}
herfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(herfamily)
print(herfamily["child2"]["name"])
for x, ob in herfamily.items():
    print(x)
    
    for y in ob:
        print(y + ':', ob[y])