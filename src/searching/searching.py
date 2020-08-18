def linear_search(arr, target):
    # Your code here
    for i in arr:
        if i == target:
            return arr.index(target)
    
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr)

    # check if arr is empty
    if not len(arr):
        return -1

    while low<= high:
        midpoint = round((high+low)/2)
        # target is on the right side
        if target > arr[midpoint]:
            low = midpoint +1
        # target is on the left side
        if target < arr[midpoint]:
            high = midpoint -1
        # target is equal to our arr[midpoint] value
        else:
            return arr.index(target)


    return -1 # not found


arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]

print(linear_search(arr1, 6))
print(linear_search(arr1, -6))

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
arr2 = []
print(binary_search(arr1, -8))
print(binary_search(arr1, 0))
print(binary_search(arr2, 6))
print(binary_search(arr2, 0))