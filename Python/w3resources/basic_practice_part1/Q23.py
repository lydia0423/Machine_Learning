
#?23. Write a Python program to get the n (non-negative integer) copies 
#?of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

def copy_string(str, n):
    result = ""
    for i in range(n):
        if(len(str) < 2):
            result = result + str
        else:
            result = result + str[:2]
    return result

print(copy_string("Hello", 2))
print(copy_string("W", 2))