""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """
""" values = [1,2.23,5,7,2,30,15]
print(values[0])
print(values[6]) """
""" 
x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """
""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """
""" x = "test"
print(f"hello {x}") """
""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """   
""" def evenorodd():
    x = int(input("give me a number"))
    if  x % 2 == 0:
        print("even")
    if  x % 1 == 0:
        print("odd")
evenorodd() """


""" bill = 100
tip_amount = int(input("Your total is 100$, would you like to tip?"))
def tip_quality():
    print(f"Your total amount is{100+tip_amount}")
    if tip_amount <= 0:
        print("Bad tip")
    elif tip_amount <= 15:
        print("Okay tip")
    elif tip_amount <= 20:
        print("Good Tip")
    elif tip_amount >= 25:
        print("Great Tip")
tip_quality()
 """

""" def factor(x):
    print("the factors of", x,"are")
    for i in range(1,x + 1):
        if x % i == 0:
            print(i)

number = 100

factor(number) """

""" import math 
x = int(input("Give me a number"))
y = int(input("Give me another number"))
print(math.gcd(x, y)) """