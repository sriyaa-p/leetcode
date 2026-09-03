class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=[] #initialise an empty array
        nums.sort()
        for i,num in enumerate(nums):
            # check for duplicate
            if i>0 and num==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                threeSum=num+nums[left]+nums[right]
                if threeSum>0:
                    right-=1
                elif threeSum<0:
                    left+=1
                else:
                    #vimp - to avoid duplicate triplets
                    result.append([num,nums[left],nums[right]])
                    left+=1
                    # If the new left value is the same as the previous left value, keep moving left forward.
                    while nums[left]==nums[left-1] and left<right: 
                        left+=1
        return result
