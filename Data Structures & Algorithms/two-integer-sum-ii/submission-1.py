class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out=[]
        l=0
        r=len(numbers)-1
        while l<r :
            s=numbers[l]+numbers[r]
            if s>target:
                r-=1
            elif s<target:
                l+=1
            else:
                out.append(l+1)
                out.append(r+1)
                return out
        