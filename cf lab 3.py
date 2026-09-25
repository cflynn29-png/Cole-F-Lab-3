
#addition function
def add(x,y):
    print(x+y)

#subtraction function
def subtract(x,y):
    print(x-y)

#multiplication function
def multiply(x,y):
    print(x*y)


#division function
def divide(x,y):
    print(x/y)

while(True):
    print("type to: (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit ")

    action=input("")

    if action == "q":
        print("calc you later!")
        break

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    if action == "a":
        add(x,y)

    if action == "s":
        subtract(x,y)

    if action == "m":
        multiply(x,y)

    if action == "d":
        divide(x,y)

