def SubArrays(arr):
    sum_map = {}
    curr_sum = 0
    result = []
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0:
            result.append((0, i))
        if curr_sum in sum_map:
            for start in sum_map[curr_sum]:
                result.append((start + 1, i))
        if curr_sum not in sum_map:
            sum_map[curr_sum] = []
        sum_map[curr_sum].append(i)
    return result
arr = [1, 2, -3, 3, -1, 2]
result = SubArrays(arr)
print(result)
