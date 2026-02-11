""" def is_discount_allowed(is_Member, age, is_Resident):
    if  age  < 12 or age >= 65:
        is_discount_allowed = input("How old are you?")
    if is_discount_allowed == "is_senior_or_child":
        print("discount nice!")
    else:
        is_discount_allowed = ("Are you a member?")
    if is_discount_allowed == "yes":
                print("discount nice!")
    else: 
        is_discount_allowed = input("Are you a resident?")
    if is_discount_allowed == "yes":
            print("discount nice!")
    else:
            print("no discount nice!")
is_discount_allowed(is_Member=True, age=True, is_Resident=True)



 """
