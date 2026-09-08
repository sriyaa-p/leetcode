class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        #Using Python inbuilt logic and the same array
        '''
        nums[::2]=sorted(nums[::2])
        nums[1::2]=sorted(nums[1::2],reverse=True)
        return nums
        '''

        #Using two arrays Even and Odd takes up more space. Brute force approach
        even=[]
        odd=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)

        j=0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=even[j]
                j+=1
        j=0
        for i in range(len(nums)):
            if i%2!=0:
                nums[i]=odd[j]
                j+=1
        return nums