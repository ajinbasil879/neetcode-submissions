class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        g={}
        for i in s:
            h[i]=h.get(i,0)+1
        for i in t:
            g[i]=g.get(i,0)+1
        return h==g
        
        