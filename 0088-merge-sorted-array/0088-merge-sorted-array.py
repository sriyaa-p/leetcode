class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Arrays are sorted in Ascending order
        # m=number of elements in nums1 and n=number of elements in nums2
        nums1 [m: ] = nums2
        nums1.sort()