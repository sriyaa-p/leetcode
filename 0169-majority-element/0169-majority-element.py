class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map={}
        #pre-compute the hashmap
        for i,num in enumerate(nums):
            hash_map[num]=hash_map.get(num,0)+1
        # Find the Majority Elements
        for num in hash_map:
            if hash_map[num]>len(nums)//2:
                return num