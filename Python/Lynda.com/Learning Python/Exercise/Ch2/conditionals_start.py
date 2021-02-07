#
# Example file for working with conditional statements
#


def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    if(x < y):
        st = "x is less than y"
    elif(x == y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"

    print(st)
    
    # conditional statements let you use "a if C else b"
    st = "x is less than y" if(x<y) else "x is greater than or the same as y"
    print(st)


#Every Python module has it’s __name__ defined and if this is ‘__main__’, it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.
#If you import this script as a module in another script, the __name__ is set to the name of the script/module.
#Python files can act as either reusable modules, or as standalone programs.
#if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.
if __name__ == "__main__":
    main()
