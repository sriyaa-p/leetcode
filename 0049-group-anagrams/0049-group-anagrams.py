class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        #Method 1: Sorting and Sorted value = Common Key This case has a time complexity of O(n x klogk)
        #create an empty hash_map
        hash_map={}
        for word in strs:
            key=" ".join(sorted(word)) # splits the word eg: "eat" -> ["a","e","t"] -> "aet"
            if key not in hash_map:
                hash_map[key]=[]
            hash_map[key].append(word)
        return list(hash_map.values())
        '''

        #Method 2: Make a tuple - O(nxk) is the time complexity
        hash_map={}
        for word in strs:
            count=[0]*26 #considering only lower case letters
            for char in word:
                index=ord(char)-ord('a')
                count[index]+=1
            key=tuple(count)
            if key not in hash_map:
                hash_map[key]=[]
            hash_map[key].append(word)
        return list(hash_map.values())
