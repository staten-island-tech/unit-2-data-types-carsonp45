def is_discount_allowed(is_Member, age, is_Resident):
    is_senior_or_child = (age  < 12) or (age >= 65)
    is_discount_allowed = input("Do you get a discount?")
    if is_discount_allowed == "is_Member":
        print("discount nice!")
    elif is_discount_allowed == "is_Resident":
        print("discount nice!")
    elif is_discount_allowed == "is_senior_or_child":
        print("discount nice!")
    else: 
        print("no discount nice!")
is_discount_allowed(is_Member=True, age=True, is_Resident=True)