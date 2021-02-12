
#?Write a password generator in Python. Be creative with how you generate passwords 
#?- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
#?The passwords should be random, generating a new password every time the user asks for a new password. 
#?Include your run-time code in a main method.

#?Extra:
#?Ask the user how strong they want their password to be. 
#?For weak passwords, pick a word or two from a list.

import random
import string

a = ["Admin", "Password", "123"]

def passowrd_generator(n, size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    if n == "Strong":
	    return ''.join(random.choice(chars) for _ in range(size))
    return random.choice(a)

def main():
   n = input("Please enter the level of password (Weak/ Strong): ")
   print(passowrd_generator(n)) 
   

if __name__ == '__main__': main()
