class Solution:
    def isValid(self, s: str) -> bool:
        t={")":"(","]":"[","}":"{"}
        out=[]
        for i in s:
            if i in t:
                if out and out[-1]==t[i]:
                    out.pop()
                else:
                    return False
            else:
                out.append(i)
        return True if not out else False

        