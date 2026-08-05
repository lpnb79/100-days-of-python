def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

mathfuncs = {
    "+": add, 
    "-": sub, 
    "*": mult, 
    "/": div
    }

num1 = float(input("Enter the first number: "))
continuingMath = True

def calculator():
    while continuingMath:
        for symbol in mathfuncs:
            print(symbol)
        op = input("Pick an operator: ")
        num2 = float(input("Enter the second number: "))
        result = mathfuncs[op](num1, num2)
        print(f"{num1} {op} {num2} = {result}")

        choice = input(f"Type 'y' to continue with {result} or 'n' to stop.  ").lower()

        if choice == 'y':
            num1 = result
        else:
            continuingMath = False
            print("\n" * 20)
            calculator()

calculator()


############## practice code

# def formatName(fname, lname):
#     fname = fname.title()
#     lname = lname.title()
#     # return f'{fname} {lname}'
#     print(f'{fname} {lname}')

# formatName(fname="lucas", lname="napier")
# # str = formatName(fname="lucas", lname="napier")
# # print(str)