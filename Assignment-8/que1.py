class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        prev = [0] * (m+1)
        cur = prev.copy()
        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]: cur[j+1] = prev[j] + ord(s1[i])
                else: cur[j+1] = max(cur[j], prev[j+1])
            prev, cur = cur, prev
        return sum(map(ord, s1+s2)) - 2 * prev[-1]