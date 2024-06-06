import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters''')

characterList = ""

# Getting character set for password
for i in range(length):
	choice = int(input("Pick a number "))
	if(choice == 1):
		
		# Adding letters to possible characters
		characterList += random.choice(string.digits)
	elif(choice == 2):
		
		# Adding digits to possible characters
		characterList += random.choice(string.ascii_letters)
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		characterList += random.choice(string.punctuation)
	else:
		print("Please pick a valid option!")
    

print(f"characterList: {characterList}")
pw=list(characterList)
random.shuffle(pw)
S="".join(pw)
print(f'PassWord: {S}')

