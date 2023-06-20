class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        n = len(candyType)

        allowed = int(n/2)

        types = len(set(candyType))

        if types<=allowed:
            return types

        else:
            return allowed