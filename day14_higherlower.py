from day14ART import logo, vs 
from day14game_data import data
import random


game = True
score = 0

subjectA = random.choice(data)
subjectB = random.choice(data)
if subjectB == subjectA:
    subjectB = random.choice(data)

def format_strings(subject):
    name = subject["name"]
    description = subject["description"]
    country = subject["country"]
    return f"{name}, a {description}, from {country}."

while game:
    
    print(logo)
    if score >= 1:
        print(f"You were right! Current score {score}.")
    else:
        print(f"Current score {score}.")

    print(f"Compare A: {format_strings(subjectA)}")

    print(vs)

    print(f"Against B: {format_strings(subjectB)}")

    aFollowers = subjectA['follower_count']
    bFollowers = subjectB['follower_count']
    choice = input("Who has more followers, A or B. ").lower()

    if choice == "a":
        choice = aFollowers
        if aFollowers > bFollowers:
            score +=1
        else:
            game = False
                        
    elif choice == "b":
        choice = bFollowers
        if bFollowers > aFollowers:
            score +=1
        else:
            game = False

    subjectA = subjectB
    subjectB = random.choice(data)
    if subjectB == subjectA:
        subjectB = random.choice(data)
            
            
print("\n" * 20)
print(logo)
print(f"You were wrong. Final score: {score}\n")
    

