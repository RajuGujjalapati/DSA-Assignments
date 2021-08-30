"""Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements 
if they are in wrong order."""


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            # reason for len(arr)-i-1
            # in the first iteration we can get max element at end.
            # so no need to traverse that element again, likewise
            # Any way its in end, no need to compare that one.
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [89,56,78,65,90,1,34,23]
print(bubble_sort(arr))
# time complexity --O(n^2)

# we can go for optimized approach
# if the inner loop doesn't change means it's already sorted.

def modified_bs(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped =True
        if swapped == False:
            break
    return arr

array = [3,32,45,2,522,43,435,53,21,23]
print(modified_bs(array))

# tc --> O(n*n) if arr is reversed
# best case --> O(n) if sorted



# recursive approach of bubble sort

class Solution:
    def __init__(self, arr):
        self.array = arr
        self.length = len(arr)
    def recursive_bs(self,n=None):
        if n is None:
            n = self.length
        if n==1:
            return 
        for i in range(n-1):
            if self.array[i] > self.array[i+1]:
                self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
        
        self.recursive_bs(n-1)

r_arr = [23,43,21,543,3,8,6,4544,34342,434]
sorting = Solution(r_arr)
sorting.recursive_bs()
print(r_arr)



        