class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        for i in nums:
            if i-1 not in nums:
                s=i
                l=1
                while s+1 in nums:
                    s+=1
                    l+=1
                longest=max(l,longest)
        return longest
            
        