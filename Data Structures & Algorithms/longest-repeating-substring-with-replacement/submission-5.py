class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h={}
        i=0
        j=0
        diff=0
        while i<=j and i<len(s) and j<len(s):
            h[s[j]]=h.get(s[j],0)+1
            d=(j-i+1)-max(h.values())
            if d>k:
                h[s[i]]=h.get(s[i],0)-1
                i+=1
            else:
                o=j-i+1
                diff=max(o,diff)
            j+=1
            
        return diff