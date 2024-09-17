def longest_common_prefix(strs):
    if not strs:
        return "-1"
    strs.sort()
    first = strs[0]
    last = strs[-1]
    min_len = min(len(first), len(last))

    i = 0
    while i < min_len and first[i] == last[i]:
        i += 1
    if i == 0:
        return "-1"

    return first[:i]

strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))
