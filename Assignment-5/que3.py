class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        return sorted(list(map(lambda n:n**2, nums)))