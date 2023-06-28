class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        mat = []
        l = []
        count=0

        if m*n != len(original):
            return []

        for i in original:

            if count<n:
                l.append(i)
                count+=1
                
            else:
                count=1
                mat.append(l)
                l = [i]
        mat.append(l)
        
        return mat