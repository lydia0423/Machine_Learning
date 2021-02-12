
#?24. Write a Python program to test whether a passed letter is a vowel or not.

def find_vowel(char):
    result = ""
    if(char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        print("{} is vowel".format(char))
    else:
        print("{} is consonant".format(char))

    return result

print(find_vowel("a"))
print(find_vowel("b"))