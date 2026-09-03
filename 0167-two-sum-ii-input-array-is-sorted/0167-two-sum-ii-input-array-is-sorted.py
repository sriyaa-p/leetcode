class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for i,num in enumerate(numbers, start=1):
            complement=target-num
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[num]=i
        return []