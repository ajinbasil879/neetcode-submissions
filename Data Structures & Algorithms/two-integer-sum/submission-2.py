class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i,a in enumerate(nums):
            diff=target-a
            if diff in m:
                return [m[diff],i]
            m[a]=i