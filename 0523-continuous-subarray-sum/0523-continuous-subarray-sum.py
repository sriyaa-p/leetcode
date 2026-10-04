class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        #initialise the value of prefix_sum
        prefix_sum=0
        #initialise the hashmap
        prefix_count={0: -1}

        for i,num in enumerate(nums):
            prefix_sum+=num
            remainder = prefix_sum%k
            if remainder in prefix_count:
                if i-prefix_count[remainder]>=2:
                    return True
            else:
                prefix_count[remainder]=i
        return False