class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        #using a frequnecy hashmap approach
        # But this method has a O(n) space complexity
        '''
        hashmap={}
        for i,num in enumerate(nums):
            hashmap[num]=hashmap.get(num,0)+1
        for num in range(len(nums)+1):
            if hashmap.get(num,0)==0:
                return num
        '''
        # Trying to implement using O(1) space complexity
        # Find the sum of the numbers in the array using the sum of the array formula -> n(n+1)/2
        # Actual is the sum of the given array
        # Missing number is Exoected-actual 

        n=len(nums)
        expected = n*(n+1)//2
        actual = sum(nums)
        return expected-actual