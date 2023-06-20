class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        n = len(nums)
        nsum=0

        for i in range(0,n-1,2):
            nsum += min(nums[i],nums[i+1])

        return nsum