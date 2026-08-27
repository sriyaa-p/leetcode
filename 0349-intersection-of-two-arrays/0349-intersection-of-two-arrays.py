class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        This is a Brute Force Solution of Time Complexity of O(NXM) or O(N^2)
        result=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    if nums1[i] not in result:
                        result.append(nums1[i])
        return result
        '''
        '''
        #Better Solution is Using Hashset
        hash_set=set(nums1)
        result=[]
        for num in nums2:
            if num in hash_set and num not in result:
                result.append(num)
        return result
        '''
        # Shortest Python Solution
        return list(set(nums1)&set(nums2))