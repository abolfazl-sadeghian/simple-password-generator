#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_length = nr_letters + nr_symbols+ nr_numbers
print(f"Password length is {password_length}")

password = []

for x in range(0,nr_letters):
  x = letters[random.randint(0,len(letters)-1)]
  password.append(x)

for x in range(0, nr_symbols):
  x = symbols[random.randint(0,len(symbols)-1)]
  password.append(x)

for x in range(0,nr_numbers):
  x = numbers[random.randint(0,len(symbols)-1)]
  password.append(x)

random.shuffle(password)

final_password = ""

for char in password:
  final_password += char

print(f"Here is your password : {final_password}")


