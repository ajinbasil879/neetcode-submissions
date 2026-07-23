class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i=0
        j=len(arr)-1
        while j-i >=k:
            if arr[j]-x > x-arr[i]:
                j-=1
            elif arr[j] - x <x-arr[i]:
                i+=1
            else:
                j-=1
        return arr[i:j+1]
        