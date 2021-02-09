
#?Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, 
#?and print out the results to the screen. I have a .txt file for you, if you want to use it!

#?Extra:
#?Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, 
#?and count how many of each “category” of each image there are. This text file is actually a list of files 
#?corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for 
#?the images. Once you take a look at the first line or two of the file, it will be clear which part represents 
#?the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. 
#?I talked a little bit about it in this post.

#Simple version
names = {}

def count_name(line):
    global names
    if line in names.keys(): 
        names.update({line : names.get(line) + 1})
    else:
        names.update({line:1})

if __name__ == "__main__":
    open_file = open('Name(Q22).txt', 'r')
    lines = open_file.readlines()
    for line in lines:
        count_name(str(line).rstrip())

    print(names)
    open_file.close() 

#Extra
categories = {}
parts = [] 

def count_catagory(line):
    global categories
    if line in categories.keys(): 
        categories.update({line : categories.get(line) + 1})
    else:
        categories.update({line:1})

if __name__ == "__main__":
    open_file = open('Extra(Q22).txt', 'r')
    lines = open_file.readlines()

    for line in lines:
        parts = line.split('/')
        count_catagory(parts[2])

    for k, v in categories.items(): 
        print(str(k) + ' : ' + str(v))
    open_file.close() 