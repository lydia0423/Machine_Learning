
#?Ask the user for a number and determine whether the number is prime or not. 
#?(For those who have forgotten, a prime number is a number that has no divisors.). 
#?You can (and should!) use your answer to Exercise 4 to help you. 
#?Take this opportunity to practice using functions, described below.

n = int(input("Please enter a number: "))

def prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:  
                print("{} is not a prime number".format(n))  
                break  
        else:  
            print("{} is a prime number".format(n))   
         
    else:  
        print("{} is not a prime number".format(n))    

print(prime(n))