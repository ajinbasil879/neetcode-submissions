class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        r= l[::-1]
        
        if l == r:
            return True
        return False