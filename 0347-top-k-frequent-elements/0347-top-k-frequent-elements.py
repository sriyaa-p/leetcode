class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Method uses a O(nlogn) time complexity
        hashmap={}
        for i,num in enumerate(nums):
            hashmap[num]=hashmap.get(num,0)+1
        sorted_nums=sorted(hashmap,  key=hashmap.get, reverse=True)
        return sorted_nums[:k]
        '''
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        # create bucket
        bucket=[[] for _ in range(len(nums)+1)]
        # add to bucket
        for num,freq in hashmap.items():
            bucket[freq].append(num)
        # Highest Frequency first
        result=[]
        for freq in range(len(nums),0,-1):
            for num in bucket[freq]:
                result.append(num)
                if len(result)==k:
                    return result