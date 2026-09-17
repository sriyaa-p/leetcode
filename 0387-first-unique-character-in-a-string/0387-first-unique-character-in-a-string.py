class Solution:
    def firstUniqChar(self, s: str) -> int:
        left=0
        hashmap={}
        for char in s:
            if char not in hashmap:
                hashmap[char]=1
            else:
                hashmap[char]+=1
        for left in range(len(s)):   
            if hashmap[s[left]]==1:
                return left
        return -1