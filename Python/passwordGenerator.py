import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

userNrOfLetters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letterChunck = []
for x in range(int(userNrOfLetters)):
    
    letterChunck.append(random.choice(letters))

print(letterChunck)

symbolChunck = []
for i in range(int(nr_symbols)):
    symbolChunck.append(random.choice(symbols))
print(symbolChunck)

numberChunck = []
for a in range(int(nr_numbers)):
    numberChunck.append(random.choice(numbers))
print(numberChunck)

password = letterChunck + symbolChunck + numberChunck
random.shuffle(password)

listToStr = ' '.join([str(elem) for elem in password])
print(listToStr)

# print(letterChunck)
# print(symbolChunck)
# print(numberChunck) 





