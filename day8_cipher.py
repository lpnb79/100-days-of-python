import day8_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(day8_art.logo)

def caeser(original_text, shift_amount, encodeOrDecode):
    output = ""
    if encodeOrDecode == "encode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output += letter
        else:
            newposition = alphabet.index(letter) - shift_amount
            newposition %= len(alphabet)
            output += alphabet[newposition]
            
    print(f"The {encodeOrDecode}d result is: {output}")
        
cont = True
while cont:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    choice = input("Continue? yes or no: \n")
    if choice.lower() == "no":
        print("Goodbye.")
        cont = False
    elif choice.lower() == "yes":
        cont = True
    else:
        print("You didn't type yes or no. Starting over anyways.\n")



############### building block of caeser function  ##########################

# def encrypt(original_text, shift_amount):
#     output = ""
#     for letter in original_text:
#         encryptedletter = alphabet.index(letter) + shift_amount
#         encryptedletter %= len(alphabet)
#         output += alphabet[encryptedletter]

#     print(f"Here is the result: {output}")

# def decrypt(original_text, shift_amount):
#     output = ""
#     for letter in original_text:
#         decryptedletter = alphabet.index(letter) - shift_amount
#         decryptedletter %= len(alphabet)
#         output += alphabet[decryptedletter]
    
#     print(f"The word is: {output}")

######################################################

####### PRACTICING BELOW HERE


# def calculate_love_score(name1, name2):
#     T = []
#     R = []
#     U = []
#     E = []
#     L = []
#     O = []
#     V = []
    
#     name1total = 0
#     name2total = 0

#     for i in (name1.lower() + name2.lower()):
#         if i == "t":
#             T.append(i)
#             name1total += 1
#         elif i == "r":
#             R.append(i)
#             name1total += 1
#         elif i == "u":
#             U.append(i)
#             name1total += 1
#         elif i == "e":
#             E.append(i)
#             name1total += 1
#             name2total += 1
#         elif i == "l":
#             L.append(i)
#             name2total += 1
#         elif i == "o":
#             O.append(i)
#             name2total += 1
#         elif i == "v":
#             V.append(i)
#             name2total += 1

#     print(f"T occurs {int(len(T))} times\nR occurs {int(len(R))} times\nU occurs {int(len(U))} times\nE occurs {int(len(E))} times\nTotal = {name1total}")

#     print(f"L occurs {int(len(L))} times\nO occurs {int(len(O))} times\nV occurs {int(len(V))} times\nE occurs {int(len(E))} times\nTotal = {name2total}")

#     loveScore = str(name1total) + str(name2total)
#     print(loveScore)

# calculate_love_score("Kanye West", "Kim Kardashian")



# def greet():
#     print("hello")
#     print("hello")
    
# greet()

# def greetWithName(name):
#     print(f"hello {name}")
#     print(f"how are you {name}")
  
# greetWithName("Lucas")

# def life_in_weeks(age):
#     weeks = (90 - int(age)) * 52
#     print(f"You have {weeks} left.")
    
# life_in_weeks(32)

# #functions with multiple inputs
# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"you are from {location}")

# greet_with("lucas", "corbin")
# greet_with(location="corbin", name="lucas")
