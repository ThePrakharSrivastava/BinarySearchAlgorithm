#Code reference taken from https://www.geeksforgeeks.org/binary-search/

# Python3 code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

import time

def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l) // 2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1
  
# Driver Code 

input_arr = []
for i in range(1, 9000009):
    input_arr.append(i)

#print(input_arr)

#arr = [ 2, 3, 4, 10, 40, 66, 72, 84, 99, 101, 115, 120, 126, 134, 138, 145, 149, 153, 154, 157, 160, 163, 165, 166, 171, 177, 178, 183, 183, 189, 191, 194, 199 ] 
arr = input_arr

x = 9000008
  
# Function call 
start_time = time.time_ns()

result = binarySearch(arr, 0, len(arr)-1, x) 
  
end_time = time.time_ns()

print("--- %s nano seconds taken by this algorithm ---" % (end_time - start_time))

if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 