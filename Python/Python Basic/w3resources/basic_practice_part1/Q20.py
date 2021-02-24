
#?20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def copy_str(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result

print(copy_str("hello", 3))
print(copy_str("world", 2))