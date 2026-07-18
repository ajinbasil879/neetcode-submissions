class Solution:
    def maxArea(self, heights: List[int]) -> int:
        large=0
        l=0
        r=len(heights)-1
        while l<r :
            a=(r-l)*min(heights[l],heights[r])
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            large=max(large,a)
        return large