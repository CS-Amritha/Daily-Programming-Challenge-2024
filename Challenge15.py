def longest_unique_substr(s):
    n = len(s)
    last_pos = {}
    start = 0
    max_len = 0

    for end in range(n):
        ch = s[end]
        if ch in last_pos:
            start = max(start, last_pos[ch] + 1)
        last_pos[ch] = end
        max_len = max(max_len, end - start + 1)

    return max_len

def main():
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "abcdefgh"
    ]

    for s in test_cases:
        result = longest_unique_substr(s)
        print(f"Input: {s}\nOutput: {result}\n{'-' * 20}")

if __name__ == "__main__":
    main()
