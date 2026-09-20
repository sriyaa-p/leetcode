class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        #using a frequnecy hashmap approach
        hashmap={}
        for i,num in enumerate(nums):
            hashmap[num]=hashmap.get(num,0)+1
        for num in range(len(nums)+1):
            if hashmap.get(num,0)==0:
                return num