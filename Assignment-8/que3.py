class Solution:
    def minDistance(self, W1: str, W2: str) -> int:

        m, n = len(W1), len(W2)

        if m < n: W1, W2, m, n = W2, W1, n, m
        dpl, dpc = [0] * (n + 1), [0] * (n + 1)

        for c1 in W1:
            for j in range(n):
                dpc[j+1] = dpl[j] + 1 if c1 == W2[j] else max(dpc[j], dpl[j+1])
                
            dpl, dpc = dpc, dpl
        return m + n - 2 * dpl[n]