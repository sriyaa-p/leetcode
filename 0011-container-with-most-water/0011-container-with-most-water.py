class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        maxArea=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            maxArea=max(maxArea,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea