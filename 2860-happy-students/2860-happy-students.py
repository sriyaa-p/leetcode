class Solution:
    def countWays(self, nums: List[int]) -> int:
        # Length of array nums = n => n=len(nums), n=total number of students in class
        # select group of students so that they remain happy
        #conditions : Returns True if one of the Two is met
        # k = Number of selected Students
        # if k>nums[i] or k<nums[i]
        # return number of ways to make the students happy

        #step 1 sort the array 
        nums.sort()
        n=len(nums)
        count=0

        for k in range(n+1):
            if k==0:
                if nums[0]>0:
                    count+=1
            elif k==n: 
                # if selected students = total students
                if nums[n-1]<n:
                    count+=1
            elif nums[k-1]<k and k<nums[k]:
                count+=1
        return count