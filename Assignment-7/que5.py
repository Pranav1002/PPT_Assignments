class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        l = list(s)
        p = 0
        n = len(s)

        while(p<n):
            if p+k<=n:
                l[p:p+k] = l[p:p+k][::-1]

            else:
                l[p:] = l[p:][::-1]

            p+=2*k

        return ''.join(l)