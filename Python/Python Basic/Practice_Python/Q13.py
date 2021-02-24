
#?Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
#?Take this opportunity to think about how you can use functions. 
#?Make sure to ask the user to enter the number of numbers in the sequence to generate.
#?(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is 
#?the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

qty = input("How many Fibonacci numbers would you like to generate?: ") 
fibonacciSequence = []

def createFibonacci(qty):
    global fibonacciSequence
    count = 0 
    print("\nFibonacci sequence:")
    while count < int(qty):
        if (len(fibonacciSequence)==0):
            fibonacciSequence.append(0)
            count += 1
        if (len(fibonacciSequence)==1):
            fibonacciSequence.append(1)
            count += 1
        if len(fibonacciSequence) >= 2:
            nextVal = (fibonacciSequence[len(fibonacciSequence)-1] + fibonacciSequence[len(fibonacciSequence)-2])
            fibonacciSequence.append(nextVal)
        count += 1

def displayFibonacciSequence():
    global fibonacciSequence
    for x in fibonacciSequence: 
        print(x) 

createFibonacci(qty) 
displayFibonacciSequence() 


        

