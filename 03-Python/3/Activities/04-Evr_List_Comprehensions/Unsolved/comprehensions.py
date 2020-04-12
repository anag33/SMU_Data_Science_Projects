# @TODO: Your code here
fish = "tilapia"

letters = []

for letter in fish:
    letters.append(letter)

print(letters)


letters = [letter for letter in fish]
print(letters)

capital_letters = []

for letter in fish:
    capital_letters.append(letter.upper())

print(capital_letters)

capital_letters = [letter.upper() for letter in fish]
print(capital_letters)


