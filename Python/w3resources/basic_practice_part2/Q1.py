
#?1. Write a Python function that takes a sequence of numbers and determines whether 
#?all the numbers are different from each other. 

def test_data(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False

print(test_data([1, 2, 3, 4, 5]))
print(test_data([2, 4, 2, 4, 5]))