import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
length = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like?\n"))
no_numbers = int(input("How many numbers would you like?\n"))

# Easy Level

password = ""

for char in range(length - no_numbers - no_symbols):
    password += random.choice(letters)

for char in range(no_symbols):
    password += random.choice(symbols)

for char in range(no_numbers):
    password += random.choice(numbers)

print(password)

# Hard Level

password = []

for char in range(length):
    password.append(random.choice(letters))


random_sample = random.sample(range(0, length), no_numbers + no_symbols)
print(random_sample)

random_sample_symbs = random_sample[:no_symbols]
print(random_sample_symbs)

random_sample_nums = random_sample[no_symbols:]
print(random_sample_nums)

for char in random_sample_symbs:
    password[char] = random.choice(symbols)

for char in random_sample_nums:
    password[char] = random.choice(numbers)

print("".join(password))

# Without length

no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like?\n"))
no_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for char in range(no_letters):
    password_list.append(random.choice(letters))

for char in range(no_symbols):
    password_list.append(random.choice(symbols))

for char in range(no_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
print(password_list)

print("".join(password_list))
