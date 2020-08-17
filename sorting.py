
arr = [99, 98, 4, 0, 5, 2, 3, 1]


# O(n)
def find_num(arr, target_num):
    for x in arr:
        if x == target_num:
            return x
        return -1 

find_num(arr, 1)

arr = [0,1 ,2 ,3 ,4 ,5 , 98, 99]


arr = [99, 98, 5, 2, 3, 1, 0 , 4]
current_element = 98
# Pseudocode for insertion sort
def insertion_sort(arr):
    ## start looping at the second element
    for idx in range(1, len(arr)): # O(n)
        ## pick up the current element and hold it
        current_element = arr[idx] # O(1)
        current__idx = idx # O(1)
        ## while current element is less than its left sibling, swap
        while current__idx > 0 and current_element < arr[current__idx - 1]: # O(n)
            ## copy left sibling to the right
            arr[current__idx] = arr[current__idx-1]
            ## decrement index
            current__idx -= 1
        ## finally, put our current element down
        arr[current__idx] = current_element

# time complexity of insertion sort?
#  n * (1+1+ (n * 2) +1)
# n * (3 + 2n)
# 3n + 2n^2
# O(n + n^2)
# ~O(n^2)

insertion_sort(arr)
print(arr)

# Pythonic way to swap values: arr[i], arr[i - 1] = arr[i - 1], arr[i]

