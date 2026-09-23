class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        minValue=nums[0] #Assume that the first element is the smallest number initially
        maxDifference=-1
        for i in range(1,len(nums)):
            if nums[i]>minValue:
                difference=nums[i]-minValue
                maxDifference=max(difference, maxDifference)
            minValue=min(minValue,nums[i])
        return maxDifference