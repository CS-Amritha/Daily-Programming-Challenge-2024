def find_first_k_repeats(nums, k):
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    for n in nums:
        if freq[n] == k:
            return n
    return -1
nums = [3, 1, 4, 4, 5, 2, 6, 1, 4]
k = 2
print(find_first_k_repeats(nums, k))
