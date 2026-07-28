import random

# List of all lowercase and uppercase letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of all single-digit numbers (as strings)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of common keyboard symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '=', '@', '^', '_']

print("this is a password generator")
numletters = int(input("how many letters do you want?\n"))
numsymbols = int(input("how many symbols do you want?\n"))
numnumbers = int(input("how many numbers do you want?\n"))

############## the simple version ##############
# password = ""
# for char in range(0, numletters):
#     password += random.choice(letters)

# for char in range(0, numsymbols):
#     password += random.choice(symbols)    

# for char in range(0, numnumbers):
#     password += random.choice(numbers)

# print(password)

#better version

passwordList = []
for char in range(0, numletters):
    passwordList += random.choice(letters)

for char in range(0, numsymbols):
    passwordList += random.choice(symbols)    

for char in range(0, numnumbers):
    passwordList += random.choice(numbers)

random.shuffle(passwordList)

password = ''
for i in passwordList:
    password += i

print(f"Your password is: {password}")






















####practicing

# fruits = ['apple', 'peach', 'pear']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

#list of scores and loops to find max score
# scores = [45, 67, 89, 90, 100, 34, 56]

# maxScore = 0

# for score in scores:
#     if score > maxScore:
#         maxScore = score

# print(maxScore)
# print(max(scores))
    
# sum = 0
# for num in range(1,101):
#     sum += num
# print(sum)