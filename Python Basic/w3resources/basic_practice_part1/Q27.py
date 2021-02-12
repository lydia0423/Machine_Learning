
#?27. Write a Python program to concatenate all elements in a list into a string and return it.

def concatenate_element(list):
    result = ""
    for i in list:
        result = result + str(i)
    return result

print(concatenate_element([1, 2, 3, 4]))