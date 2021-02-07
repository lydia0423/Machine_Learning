
#?26. Write a Python program to create a histogram from a given list of integers.

def histogram(items):
    for i in items:
        output = ""
        times = i
        while(times > 0):
            output += "*"
            times -= 1
        print(output)

print(histogram([1, 2, 3, 4, 5]))
