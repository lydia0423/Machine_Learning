#
# Example file for HelloWorld
#

#use def to define a function
#python use indent/white space to define the scope of the code
def main():
    print("Hello World")
    name = input("What is your name? ")
    print("Nice to meet you,", name)


#used to make sure when the file is loaded in own program, line 14 will be called
if __name__ == "__main__":
    main()
