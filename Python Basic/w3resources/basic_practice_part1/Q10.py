
#?10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#?Sample value of n is 5
#?Expected Result : 615

value = int(input("Please enter an integer: "))
# %s: operator where string values are added.
n1 = int("%s" % value)
n2 = int("%s%s" % (value,value))
n3 = int("%s%s%s" % (value,value,value))
print(n1+n2+n3)

#* (5+5+5) = 15 (pass 1 to 10) 5
#* (5+5) = 10 (10 plus 1 equal to 11 so pass one to 5) 1
#* 5 = 5 (5 plus 1 equal to 6) 6
