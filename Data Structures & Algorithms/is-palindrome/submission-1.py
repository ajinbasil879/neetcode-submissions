class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if i.isalpha() or i.isdigit():
                l.append(i.lower())
        r= l[::-1]
        
        if l == r:
            return True
        return False