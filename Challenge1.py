def DNF_Algo(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:  # We reached the unsorted part of the array
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]  # Swap 0 to the front
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1  # Simply move to the next element
        elif arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]  # Swap 2 to the back
            high -= 1
arr = [0, 1, 2, 1, 0, 2, 1, 0]
DNF_Algo(arr)
print(arr) 


