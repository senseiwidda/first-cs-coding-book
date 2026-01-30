fruits=("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
fruits+=("orange","strawberry","raspberry")
print(fruits)
(green, yellow, *red) = fruits
print(green)
print(yellow)   
print(red)
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)