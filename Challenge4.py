#Appproach-2, gap method
def swapIfGreater(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]
def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    total_len = n + m
    gap = (total_len // 2) + (total_len % 2)
    while gap > 0:
        i = 0
        j = gap

        while j < total_len:
            if i < n and j < n:  
                swapIfGreater(arr1, arr1, i, j)
            elif i < n and j >= n:
                swapIfGreater(arr1, arr2, i, j - n)
            else: 
                swapIfGreater(arr2, arr2, i - n, j - n)
            i += 1
            j += 1
        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merge(arr1, arr2)
print("arr1:", arr1)
print("arr2:", arr2)


#Approach-1
'''def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)    
    arr3 = [0] * (n + m)
    left = right = index = 0
    while left < n and right < m:
        if arr1[left] <= arr2[right]:
            arr3[index] = arr1[left]
            left += 1
        else:
            arr3[index] = arr2[right]
            right += 1
        index += 1
    while left < n:
        arr3[index] = arr1[left]
        left += 1
        index += 1
    while right < m:
        arr3[index] = arr2[right]
        right += 1
        index += 1
    for i in range(n + m):
        if i < n:
            arr1[i] = arr3[i]
        else:
            arr2[i - n] = arr3[i]
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

merge(arr1, arr2)

print("arr1:", arr1)
print("arr2:", arr2)'''
