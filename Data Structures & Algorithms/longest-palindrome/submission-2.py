class Solution:
    def longestPalindrome(self, s: str) -> int:
        r=0
        t=[]
        for i in s:
            if i in t:
                t.remove(i)
                r+=2
            else:
                t.append(i)
        return r+1 if t else r 
        