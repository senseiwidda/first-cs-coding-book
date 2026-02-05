a=41
if a>10:
    print("Above ten,")
    if a>20:
        print("and also above 20!")
    else:
        print("but not above 20.")
age=25
has_liscense=True
if age>=18:
    if has_liscense:
        print("You can drive.")
    else:
        print("You need a liscense to drive.")
else:
    print("You are too young to drive.")

score=85
attendance=90
submitted=True
if score>=60:
    if attendance>=80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")