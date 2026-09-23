class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        # Length of the Array 
        n=len(nums)
        # sort the array
        nums.sort()
        #result or the difference
        result=nums[n-1]-nums[0]
        for i in range(1,n):
            minVal=min(nums[0]+k,nums[i]-k)
            maxVal=max(nums[i-1]+k, nums[n-1]-k)
            result=min(result, maxVal-minVal)
        return result