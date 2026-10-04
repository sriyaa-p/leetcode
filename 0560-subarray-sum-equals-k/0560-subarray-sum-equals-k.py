class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        count=0
        prefixSum_freq={0: 1}

        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in prefixSum_freq:
                count+=prefixSum_freq[prefix_sum-k]
            prefixSum_freq[prefix_sum]=prefixSum_freq.get(prefix_sum,0)+1
        return count