class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1={}
        for i in s1:
            f1[i]=f1.get(i,0)+1
        i=0
        j=len(s1)
        while i<j and i<len(s2) and j<=len(s2):
            t={}
            for c in range(i,j):
                t[s2[c]]=t.get(s2[c],0)+1
            if t==f1:
                return True
            i+=1
            j+=1
        return False
