class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # Step-1 get the length of the string:
        n=len(nums)
        #step-2 initialise dp
        dp=[1]*(n)
        # step-3 logic
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)