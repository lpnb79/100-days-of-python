print("Welcome to the Tip Calculator!")
bill = float(input("What is the total bill? $"))
tipPercent = float(input("How much tip would you like to give? Enter a number. "))
people = int(input("How many people to split the bill?  "))
totalBill = bill + (bill * (tipPercent/100))

print(f"Each person should pay ${ round((totalBill/people), 2 ) }.")
