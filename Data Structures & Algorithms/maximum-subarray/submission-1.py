class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        gmax=nums[0]
        cmax=nums[0]
        for i in range(1,len(nums)):
            cmax=max(nums[i],nums[i]+cmax)
            gmax=max(gmax,cmax)
        return gmax