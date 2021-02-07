#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while(x <5):
    print(x)
    x = x + 1


  # define a for loop
  for x in range(5,10): #start at 5 and stop at 10
    print(x)


  # use a for loop over a collection
  days= ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  #d will be set to the current item that looking at that time through the loop
  for d in days:
    print(d)

  
  # use the break and continue statements
  for x in range(5,10):
    #if(x == 7): break
    if(x % 2 == 0): continue #continue = skip rest of the loop and just go back to the top of the loop and start with next value
    print(x)


  #using the enumerate() function to get index 
  days= ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  #enumerate will return two values which are the index number of the element and the element itself
  for i,d in enumerate(days):
    print(i,d)
  
if __name__ == "__main__":
  main()
