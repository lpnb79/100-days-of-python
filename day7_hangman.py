import random
from hangman_words import word_list
from hangman_art import stages, logo


lives = 6
print(logo)
chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
for i in chosen_word:
    placeholder += "_"
print(f"{placeholder}")

gameover = False
correctLetters = []

while not gameover:
    
    guess = input("\nguess a letter: ").lower()
    print(f"You have {lives} lives left.")
    if guess in correctLetters:
        print(f"You already guessed {guess.upper()}.")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correctLetters.append(letter)
        elif letter in correctLetters:
            display += letter
        else:
            display += "_"

                    
    print(display)

    
    if guess not in chosen_word:
        lives -= 1
        print(f"\n{guess.upper()} is not in the word. Lose a life.")
        if lives == 0:
            print(f"YOU LOSE. IT WAS {chosen_word.upper()}.")
            gameover = True
            
        
    

    if "_" not in display:
        print("\nyou win")
        gameover = True

    print(stages[lives])
 