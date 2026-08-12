import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = int(random.choice(cards))
    return card

def calculate_score(cards):
    """returns score or 0 if someone gets a blackjack"""
    score = sum(cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and score > 21:
            cards.remove(11)
            cards.append(1)
            return(score)
    return score 

def compare(uPoints, cPoints):
    """ used at the end. figures out who wins the game"""
    if uPoints == cPoints:
        return print("Draw.\n")
    elif cPoints == 0:
        return  print("BLACKJACK. Computer wins.\n")
    elif uPoints == 0:
        return print("BLACKJACK. You win.\n")
    elif uPoints > 21:
        return print("You're over 21. Computer wins.\n")
    elif cPoints > 21:
        return print("Computer over 21. You win.\n")
    elif uPoints > cPoints:
        return print("You win.\n")
    else:
        return print("You lose.\n")
    
def play_game():
    print(logo)
    user_cards = []
    user_score = -1

    computer_cards = []
    computer_score = -1

    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} Your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}\n")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card or 'n' to pass. ")
            if user_deal == "y".lower():
                user_cards.append(deal_card())
            else:
                print("\n"*5)
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}\n Computer's cards: {computer_cards}\n")
    print(f"Your score: {user_score}\n Computer score: {computer_score}\n")
    compare(uPoints=user_score, cPoints=computer_score)

while input("Play Blackjack? y or n: ") == "y".lower():
    print("\n"*10)
    play_game()
