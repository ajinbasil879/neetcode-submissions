class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        t=[]
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        t=l[::-1]
        return l==t
        

        