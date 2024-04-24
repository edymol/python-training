import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

easy = []
hard = []

for _ in range(nr_letters):
    easy.append(random.choice(letters))
    hard.append(random.choice(letters))

for _ in range(nr_numbers):
    easy.append(random.choice(numbers))
    hard.append(random.choice(numbers))

for _ in range(nr_symbols):
    easy.append(random.choice(symbols))
    hard.append(random.choice(symbols))

random.shuffle(hard)

password = "".join(easy)

hard_pass = ''.join(hard)

print("easy: ", password)
print("hard: ", hard_pass)

