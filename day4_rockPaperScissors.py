import random

rps = ["rock", "paper", "scissors"]
computerChoice = random.choice(rps)


userChoice = int(input("Which do you choose? 0 = rock, 1 = paper, 2 = scissors. \n"))
``
if userChoice < 0 or userChoice> 2:
    print("You didn't pick 0, 1, or 2.\n")

else:
    print(f"You picked {rps[userChoice]}.")
    print(f"Computer picked {computerChoice}.\n")

    if userChoice == 0:
        if computerChoice == rps[0]:
            print("draw")
        elif computerChoice == rps[1]:
            print("you lose")
        else:
            print("you win")

    elif userChoice == 1:
        if computerChoice == rps[1]:
            print("draw")
        elif computerChoice == rps[2]:
            print("you lose")
        else:
            print("you win")

    elif userChoice == 2:
        if computerChoice == rps[2]:
            print("draw")
        elif computerChoice == rps[0]:
            print("you lose")
        else:
            print("you win")







#############PRACTICE CODE IS BELOW THIS LINE###########
# randInt = random.randint(1,100)
# print(randInt)

# randNum = random.random() *10 
# print(randNum)

# randFloat = random.uniform(1,10) 
# print(randFloat)

# coinFlip = random.random()*10

# if coinFlip < 5:
#     print("heads\n")

# else:
#     print("tails\n")

# #lists
# states = ["California", "Texas", "Florida", "New York", "Illinois"]

# # print(states[3])
# # print(states[-1])

# # states.append("Pennsylvania")

# # print(states)


# friends = ['alice', 'bob', 'charlie', 'david', 'eve']
# # randName = random.randint(0, len(friends)-1)
# # print(friends[randName])

# # randNamev2 = random.choice(friends)
# # print(randNamev2)

# combo = [states, friends]
# print(combo[1][1])
# # print(combo[5])

