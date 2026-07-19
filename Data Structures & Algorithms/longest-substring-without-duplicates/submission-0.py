class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        diff=0
        out=[]
        while i<=j and i<len(s)and j<len(s):
            if s[j] in out:
                out.pop(0)
                i+=1
            else:
                out.append(s[j])
                j+=1
                c=j-i
                diff=max(c,diff)
        return diff
        