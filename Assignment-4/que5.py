class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(1, n+1):
            n-=i

            if n>0:
                continue
            elif n==0:
                return i
            else:
                return i-1