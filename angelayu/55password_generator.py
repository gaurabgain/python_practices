import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password=[]

for i in range(nr_letters):
    c=random.randint(0,len(letters)-1)
    password+=letters[c]
for i in range(nr_symbols):
	c=random.randint(0,len(symbols)-1)
	password+=symbols[c]
for i in range(nr_numbers):
	c=random.randint(0,len(numbers)-1)
	password+=numbers[c]

random_password=""
for i in range(len(password)):
	c=random.randint(0,len(password)-1)
	random_password+=password[c]
	
print(f"Your random generated password is {random_password}")
#print(f"nr_letters is a {type(nr_letters)}.")
