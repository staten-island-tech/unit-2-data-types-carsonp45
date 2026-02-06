def is_discount_allowed(is_Member, age, is_Resident):
    if(is_Member or is_Resident or age < 12 or age >= 65):
        print("discount_nice")
    else:
        print("no_discount_nice")

    
    
    
print(is_discount_allowed(True, 11, False))
    
print(is_discount_allowed(False, 45, True))