#Approach_2
def FindDuplicate(arr):
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
        return slow
arr = [1, 3, 4, 2, 2]
print(FindDuplicate(arr)) 

#Approach_1
'''def FindDuplicate(arr):
    seen = set()
    for i in arr:
        if i not in seen:
            seen.add(i)
        else:
            return i
    
arr = [1,2,3,3,4]
print(FindDuplicate(arr))'''