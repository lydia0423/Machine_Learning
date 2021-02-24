
#?59. Write a Python program to convert height (in feet and inches) to centimeters.

h_ft = float(input("Please enter the height in feet: "))
h_in = float(input("Please enter your height in inches: "))

h_in += h_ft * 12
h_cm = round(h_in * 2.54, 1)

print("Your height is : %d cm." % h_cm)