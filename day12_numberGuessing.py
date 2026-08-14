import random

RAND_NUMBER = random.randint(1,100)
GUESSES = 10


print(f"Welcome to the number guessing game.\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "hard":
    GUESSES = 5

game = True

while game:
    if GUESSES > 0:
        print(f"\nYou have {GUESSES} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == RAND_NUMBER:
            print(f"You got it, the answer was {RAND_NUMBER}.")
            game = False
        elif guess > RAND_NUMBER:
            print(f"Too high. Guess again.\n")
            GUESSES -= 1
        elif guess < RAND_NUMBER:
            print(f"Too low. Guess again.\n")
            GUESSES -= 1

    elif GUESSES == 0:
        print(f"Out of guesses. The number was {RAND_NUMBER}.")
        game = False

    

    

        #













# PRIME NUMBER FUNCTION FOR PRACTICE
# def is_prime(num):
#     factors = []
#     for i in range(1,num+1):
#         if num % i == 0:
#             factors.append(i)
    
#     if len(factors) > 2:
#         return False
#     else:
#         return True
            
        

