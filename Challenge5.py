def Leader(arr, n):
    for i in range(n):
        flag = False
        for j in range(i+1, n):
            if(arr[i] <= arr[j]):
                flag = True
                break
        else: 
            print(arr[i], end=' ')
arr = [16, 17, 4, 3, 5, 2]
Leader(arr, len(arr))

