
#?Write a function that takes an ordered list of numbers (a list where the elements are in order 
#?from smallest to largest) and another number. The function decides whether or not the given number 
#?is inside the list and returns (then prints) an appropriate boolean.

#?Extras:
#?Use binary search.

#* l = left
#* r = right

def binary_search(arr, l, r, x):
    # Check base case 
    if r >= l: 
        mid = l + (r - l) // 2

        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binary_search(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# Driver Code 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
x = 4
  
# Function call 
result = binary_search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 
