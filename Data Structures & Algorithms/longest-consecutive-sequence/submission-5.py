class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long=0
        for i in nums:
            if i-1 not in nums:
                s=i
                l=1
                while s+1 in nums:
                    s+=1
                    l+=1
                long=max(long,l)
        return long