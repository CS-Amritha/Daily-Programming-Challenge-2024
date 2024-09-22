def DistinctKSubstring(s,k):
    count={}
    left=0
    result=0    
    for right in range(len(s)):
        count[s[right]] = count.get(s[right],0)+1
        
        while len(count) > k:
            count[s[left]]-=1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1  
        result +=right-left+1
    
    return result

def countSubstrings(s,k):
    if k==0:
        return 0
    return DistinctKSubstring(s,k) - DistinctKSubstring(s,k-1)

print("input a string:")
Userinput=input()
k = int(input("input an integer k: "))
result = countSubstrings(Userinput,k)
print(result)
