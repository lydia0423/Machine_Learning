
#?Ask the user for a string and print out whether this string is a palindrome or not. 
#?(A palindrome is a string that reads the same forwards and backwards.)

word = input("Please enter a word: ")

if(word == word[::-1]):
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))
