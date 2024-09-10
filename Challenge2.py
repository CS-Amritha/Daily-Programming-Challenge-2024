#For unsorted array
def Findmissing(arr):
    n = len(arr)+1
    sumarr = 0
    for i in arr:
        sumarr = sumarr + i

    total = n*(n+1)//2
    missing = total - sumarr
    return missing
input_str = input("Enter the list of numbers separated by commas: ")
input_int = input_str.split(',')
arr = list(map(int,input_int))

print(Findmissing(arr))
#Assumes that the array is sorted
'''def FindMissing(arr):
    i = 0
    j = 1
    n = len(arr)
    for i in range(n):
        if arr[i] != j:
            return j
        
        j += 1
        
arr = [1,2,4,5]
print(FindMissing(arr)) '''





    
