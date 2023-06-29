class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        
        a.sort()
        b.sort(reverse=True)
        
        ans=0
        
        for i in range(n):
            
            ans+=a[i]*b[i]
        return ans
