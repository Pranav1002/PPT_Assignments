class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False

        p = 0
        q = len(arr)-1

        while(p<q):
            if arr[p]<arr[p+1]:
                p+=1
            elif arr[q]<arr[q-1]:
                q-=1
            else:
                return False
            
        if arr[p]==arr[q] and p!=len(arr)-1 and q!=0:
            return True
        else:
            return False