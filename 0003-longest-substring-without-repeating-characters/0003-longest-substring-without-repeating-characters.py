class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #using two pointers left and right starting at index 0
        # sliding window = should not have duplicate characters in the same window if same increment left
        # use a hashmap to map an index to the character
        left, right=0, 0
        maxlength=0
        hashmap={}
        n=len(s)
        while right<n: 
            if s[right] in hashmap:
                if hashmap[s[right]]>=left:
                    left=hashmap[s[right]]+1 #shift the window to ensure no duplicates
            length=right-left+1
            maxlength=max(length,maxlength)
            hashmap[s[right]]=right
            right+=1
        return maxlength