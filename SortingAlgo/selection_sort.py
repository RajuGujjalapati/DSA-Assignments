"""lets say if they ask find the second smallest element or first smallest element in an array
we can go for selection sort because in selction sort we are traversing all the elements and inserting 
smallest in starting position toof an array.
So if we want first/second/... smallest element we can go for selection sort"""

# time complexity : O(n^2)
# auxiliary space : O(1)

# it is not a stable algorithm --> But we can make it stable
# inplace --> True (no extra space required)

arr = [68, 55, 12, 92, 91]

for i in range(len(arr)):
    # finding the index of min element
    min_ind = i # default to 0th pos
    for j in range(i+1, len(arr)):
        if arr[min_ind] > arr[j]:
            min_ind = j # overriding min index so that we can keep eye on min number index

    # swapping min value index in first position
    arr[i], arr[min_ind] = arr[min_ind], arr[i]

print(arr)

# the above is not stable, if we have duplicates the position may vary



# stable approach

"""Selection sort can be made Stable if instead of swapping, 
the minimum element is placed in its position without swapping i.e. by placing the number in its position by pushing every element one step forward. """


def stableSelectionSort(a, n):
     
    # Traverse through all array elements
    for i in range(n):
 
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
 
        # Move minimum element at current i
        key = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = key

a = [4, 5, 3, 2, 4, 1]
n = len(a)
stableSelectionSort(a, n)
print(a)
