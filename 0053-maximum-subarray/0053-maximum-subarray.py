class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        # Brute Force - passes only 199/210 test cases as Time Complexity is O(N^3)
        max_sum=float('-inf')
        for i in range(len(nums)):
            for j in range (i, len(nums)):
                sum1=0
                for k in range(i,j+1):
                    sum1+=nums[k]
                max_sum=max(max_sum,sum1)
        return max_sum
        '''
        '''
        # Better Approach - Time Complexity O(N^2) but only passes 202 test cases
        max_sum=float('-inf')
        for i in range(len(nums)):
            sum1=0
            for j in range(i,len(nums)):
                sum1+=nums[j]
                max_sum=max(max_sum,sum1)
        return max_sum
        '''
        #Optimal using Kadane algo 
        max_sum=float('-inf')
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            if (sum1>max_sum):
                max_sum=sum1
            if sum1<0:
                sum1=0
        return max_sum