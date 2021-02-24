
#?Write a program (function!) that takes a list and returns a new list that contains all the elements 
#?of the first list minus all the duplicates.

#?Extras:
#?Write two different functions to do this - one using a loop and constructing a list, 
#?and another using sets.
#?Go back and do Exercise 5 using sets, and write the solution for that in a different function

def wList(LIST):
    l=[]
    for x in LIST:
        if x not in l:
            l.append(x)
    return l

def wSet(LIST):
    l=set(LIST)
    return list(l)

l1=[1,1,1,2,2,2,3,3,4,5,5,5,6,6,7,7,88,9,37,0]

print (wList(l1),wSet(l1))


