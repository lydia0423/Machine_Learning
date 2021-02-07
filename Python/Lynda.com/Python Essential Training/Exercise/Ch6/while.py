#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#simple for loop
secret = 'swordfish'
pw = ''

while pw != secret:
    pw = input("What's the secret word? ")

#for loop with additional controls
secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt: break
    pw = input(f"{count}: What's the secret word? ")
else:
    auth = True

#ternary condition
print("Authorized" if auth else "Calling the FBI ...")
