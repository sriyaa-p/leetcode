class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map is the Optimal approach for the given Solution when the array is not sorted
        hash_map={}
        for i,num in enumerate(nums):
            complement = target-num
            if complement in hash_map:
                return [hash_map[complement],i]
            hash_map[num]=i

        '''
        #Using two pointer approach not optimal solution takes O(nlogn) time
        indexed_nums=[(num,i) for i,num in enumerate(nums)]
        indexed_nums.sort()
        left=0
        right=len(indexed_nums)-1
        while left<right:
            current_sum=indexed_nums[left][0]+indexed_nums[right][0]
            if current_sum==target:
                return indexed_nums[left][1],indexed_nums[right][1]
            elif current_sum<target:
                left+=1
            else:
                right-=1
        return []
        '''