class Solution:
    def trap(self, height: List[int]) -> int:
        width=1
        result=0
        for i,num in enumerate(height):
            leftmax=max(height[:i+1])
            rightmax=max(height[i:])
            area=width*min(leftmax,rightmax)-height[i]  
            result=result+area
        return result