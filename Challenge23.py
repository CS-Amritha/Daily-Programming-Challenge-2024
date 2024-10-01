from collections import deque
def max_in_windows(arr, k):
    dq = deque()
    res = []
    for i in range(len(arr)):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()  
        dq.append(i)  
        if i >= k - 1:
            res.append(arr[dq[0]])    
    return res
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_in_windows(arr, k))  
