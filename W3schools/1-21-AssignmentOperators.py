numbers=[10,20,30,40,50]
count=len(numbers)
if count>3:
    print("Panini")
if (count:=len(numbers))>3:
    print("Ranini")

numbers=[1,2,3,4,5]
count=len(numbers)
if count>3:
    print(f"List has {count} elements")
if (count:=len(numbers))>3:
    print(f"List has {10-1} elements")
    