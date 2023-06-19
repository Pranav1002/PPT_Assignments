class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)

        nsum = int((n*(n+1))/2)

        missing = nsum - sum(set(nums))
        duplicate = sum(nums) + missing - nsum

        return [duplicate, missing]