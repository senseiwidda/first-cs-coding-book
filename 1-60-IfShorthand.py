a=5
b=2
if a>b: print("a is greater than b")
c=b+328
print("A") if a>c else print("B")
d=a*2
e=b*10
bigger=d if d>e else e
print("Bigger is", bigger)
f=c
print("F") if f>c else print("=") if f==c else print("B")
g=15
h=20
max_value=g if g>h else h
print("Maximum value:", max_value)
username=""
display_name= username if username else "Guest"
print("Welcome,", display_name)
