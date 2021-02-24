
#?7. Write a Python program to accept a filename from the user and print the extension of that.
#?Sample filename : abc.java
#?Output : java

filename = input("Please enter a file name with extension: ")
filename = filename.split(".")
print("The extension of the file is " + repr(filename[-1]))