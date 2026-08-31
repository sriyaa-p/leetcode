class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        # Using Kadane Algo - Dynamic Programming - passes only 112/191 test cases and insufficient 
        largest_product=float('-inf')
        product=1
        for i in range(len(nums)):
            product*=nums[i]
            if product>largest_product:
                largest_product=product
        return largest_product
        '''
        current_max=nums[0]
        current_min=nums[0]
        largest_product=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                current_max, current_min = current_min, current_max
            current_max=max(nums[i],current_max*nums[i])
            current_min=min(nums[i],current_min*nums[i])
            largest_product=max(largest_product,current_max)
        return largest_product