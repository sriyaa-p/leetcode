class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
       prefix_sum=0
       count=0
       prefix_count={0: 1}

       for num in nums:
           prefix_sum+=num
           remainder=prefix_sum%k
           if remainder in prefix_count:
              count+=prefix_count[remainder]
           prefix_count[remainder]=prefix_count.get(remainder,0)+1
       return count