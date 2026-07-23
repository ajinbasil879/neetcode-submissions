class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        s=0
        lon=float('inf')
        while i<=j and i<len(nums) and j < len(nums):
            s+=nums[j]
            while s>=target:
                l=j-i+1
                lon=min(lon,l)
                s-=nums[i]
                i+=1
            j+=1
        if lon==float('inf'):
            return 0
        return lon
            
            

            
        