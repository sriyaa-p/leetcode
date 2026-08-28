class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Method 1: Sorting and Sorted value = Common Key This case has a time complexity of O(n x klogk)
        #create an empty hash_map
        hash_map={}
        for word in strs:
            key=" ".join(sorted(word))
            if key not in hash_map:
                hash_map[key]=[]
            hash_map[key].append(word)
        return list(hash_map.values())