# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        for j in range (i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                # for loop finds smallest possible index
                smallest_index = j
    

        # TO-DO: swap
        # Your code here
        
        # swaps smallest index with current index pythonic way:
        # arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

        copy_cur_index = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = copy_cur_index
    return arr


test = [1, 5, 4, 2, 8, 6, 0, 3, 7, 9]
print(selection_sort(test))
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Your code here
    # looks at two adjacent values at the same time
    # make a for loop to compare both of those values
    for i in range(0, len(arr) -1):
        # if arr[i] > arr[i+1]:
        #     # arr[i],arr[i+1] = arr[i+1], arr[i] 
        #     copy_index_i = arr[i]
        #     arr[i] = arr[i+1]
        #     arr[i+1] = copy_index_i
        #     bubble_sort(arr)

# 2 forloops: we're going through the whole array j times, i bumps by 1,
#  going through the whole array j times again,  i+1 etc....
        for j in range(0, len(arr)-i-1):
            # NOTE: largest valye always ends up being at last index after just our first swap
            # we can reduce len(arr) by 1 every time we're running j loop again
            # -i -->  first time we go through the whole array, then whole array without last index, then without 2  last indexes, etc...
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j] 
                # copy_index_j = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = copy_index_j

    # swapped = True
    # while swapped:
    #     swapped = False
    #     for i in range(len(arr) -1):
    #         if arr[i] > arr[i+1]:
    #             arr[i], arr[i+1] = arr[i+1], arr[i]
    #             swapped = True


    return arr

test = [1, 5, 4, 2, 8, 6, 0, 3, 7, 9]
print(bubble_sort(test))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
import random
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [1, 5, -2, 4, 3]
arr4 = random.sample(range(200), 50)
def counting_sort(arr, maximum=None):
    # Your code here
    # check if array is empty
    if not len(arr):
        return arr

    for i in range(len(arr)-1):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"

    # find max value
    max_val = arr[0]
    for i in range(len(arr)-1):
        if arr[i] > max_val:
                max_val = arr[i]
    
    # initialize the array to new array of zeros of length max_val +1
    initialized_arr = []
    for i in range(max_val +1):
        initialized_arr.append(0)
    # check how many times unique values show up (index is a unique value)
    # index 0 = how many times 0 shows up, index 1 = number of 1s, etc
        for j in range(len(arr)):
            if arr[j] == i:
                initialized_arr[i] += 1

    # modify array to now include the sum of previous counts
    for i in range(1,max_val +1):
        initialized_arr[i] += initialized_arr[i-1]

    # sort the original arr:
    for i in range(max_val):

        if initialized_arr[i] < initialized_arr[i + 1]:
            count = initialized_arr[i]
            if initialized_arr[i] == initialized_arr[0]:
                arr[count-1] = i
            else:
                while count > initialized_arr[i-1]:
                    arr[count -1] = i 
                    count -=1
        if i == max_val:
            arr[i+1] = max_val
        else:
            arr[initialized_arr[i]] =i+1



    return arr

print("array1",arr1)
print("sorted array1:",counting_sort(arr1))
print(counting_sort(arr2))
print(counting_sort(arr3))
print(counting_sort(arr4))