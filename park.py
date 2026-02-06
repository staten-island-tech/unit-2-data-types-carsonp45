def is_discount_allowed(is_Member, age, is_Resident):
    is_discount_allowed = input("Do you get a discount?")
    if is_discount_allowed == "is_Member":
        print("discount nice!")
    elif is_discount_allowed == "is_Resident":
        print("discount nice!")
    elif is_discount_allowed  < 12:
        print("discount nice!")
    elif is_discount_allowed >= 65:
        print("discount nice!")
    else: 
        print("no discount nice!")
is_discount_allowed(is_Member=True, age= < 12 or >= 65, is_Resident=True)