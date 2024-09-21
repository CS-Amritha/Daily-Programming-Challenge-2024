def longest_palindrome(s: str) -> str:
    def expand(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
    if len(s) <= 1:
        return s
    res = ""
    for i in range(len(s)):
        p1 = expand(s, i, i)   
        p2 = expand(s, i, i + 1)  
        res = max(res, p1, p2, key=len)
    return res
    
print(longest_palindrome("babad")) 
print(longest_palindrome("cbbd"))  
print(longest_palindrome("a"))     
print(longest_palindrome("aaaa"))   
print(longest_palindrome("abc")) 
