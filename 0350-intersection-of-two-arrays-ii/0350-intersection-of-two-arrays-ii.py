class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map={}
        result=[]
        #counts the frequency
        for i,num in enumerate(nums1):
            hash_map[num]=hash_map.get(num,0)+1
        #Finding the Intersection
        for num in nums2:
            if hash_map.get(num,0)>0:
                result.append(num)
                hash_map[num]-=1
        return result