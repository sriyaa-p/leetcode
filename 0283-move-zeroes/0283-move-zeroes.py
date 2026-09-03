class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Using Quick Sort or Quick Select
        left=0
        for right in range(len(nums)):
            if nums[right]:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        return nums