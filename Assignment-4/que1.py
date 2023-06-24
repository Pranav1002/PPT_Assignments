from collections import Counter
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        
        
        
        p = list(set(A))+list(set(B))+list(set(C))
        
        counter = Counter(p)
        
        ans=[]
        
        for i in p:
            if counter[i]>=3 and i not in ans:
                ans.append(i)
        ans.sort()
                
        return ans