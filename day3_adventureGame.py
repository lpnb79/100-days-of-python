#adventure game
print("Welcome to Treasure Island, good luck.")
choice1 = input("\tGo left or right? ")

if choice1.lower() == "left":
    print("You avoided a horrible, painful death. You continue walking.")
    
    choice2 = input("You arrive at a shoreline and see an island. Swim there or wait for a bit...? ")
    
    if choice2.lower() == "wait":
        print("Smart...a fisherman comes by to get you. " \
        "He brings you to a mysterious house, don't ask questions.\n")
        
        choice3 = input("you see three doors, a red door, a blue door, and a yellow door...pick one. ")
        
        if choice3.lower() == "red" or "red door":
            print("you were burned alive, game over.")
        elif choice3.lower() == "blue" or "blue door":
            print("eaten by Cthulu, game over.")
        elif choice3.lower() == "yellow" or "yellow door":
            print("you win! have a piece of candy.")
        else:
            print("any other decision resulted in your instant death via random meteor from the sky.")
        
    else:
        print("that was dumb...you are eaten alive by trout. Try again.")
    
else:
    print("You fell in a hole and died. Try again.")






##pizza deliveries
#
#print("Welcome to pizza deliveries")
#size = input("what size pizza? s/m/l: ")
#pepp = input("do you want pepperoni? y/n ")
#xtracheese = input("do you want extra cheese? y/n ")
#
#total = 0
#
#if size == "s":
#    total += 15
#    if pepp == "y":
#        total += 2
#    
#elif size == "m":
#    total += 20
#    if pepp == "y":
#        total += 3
#
#elif size == "l":
#    total += 25
#    if pepp == "y":
#        total += 3
#
#else:
#    print("enter either s or m or l")
#
#if xtracheese == "y":
#        total += 1
#
#print(f"Your total is ${total}")



# print("welcome to rollercoaster")
#
#height = int(input("whats your height? "))
#totalPrice = 0
#                   
#if height > 120:
#    print("you can ride")
#    age = int(input("how old are you? "))
#    if age >= 18:
#        print("price = $12")
#        totalPrice = 12
#    elif age >=12:
#        print ("price = $7")
#        totalPrice = 7
#    else:
#        print("price = $5")
#        totalPrice = 5
#    
#    wantPhoto = input("do you want your photo? y/n ")    
#    if wantPhoto == "y":
#        print("add $3 to price")
#        totalPrice += 3
#
#    print(f"your total is ${totalPrice}")   
#
#    
#else:
#    print("you cannot ride\n")

    

