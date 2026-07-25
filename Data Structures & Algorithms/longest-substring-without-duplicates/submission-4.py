class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        diff=0
        out=[]
        while i<=j and j<len(s):
            if s[j]in out:
                out.pop(0)
                i+=1
            else:
                out.append(s[j])
                d=j-i+1
                diff=max(diff,d)
                j+=1
        return diff