class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f={}
        for i in s1:
            f[i]=f.get(i,0)+1
        l=0
        r=len(s1)
        while l<r and r<=len(s2) and l<len(s2):
            t={}
            for i in range(l,r):
                t[s2[i]]=t.get(s2[i],0)+1
            print(t)
            if t==f:
                return True
            l+=1
            r+=1
        return False
