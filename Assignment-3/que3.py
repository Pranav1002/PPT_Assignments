class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in reversed(range(0,len(nums)-1)):
            if nums[i]>=nums[i+1]:
                continue

            next = i+1

            while next<len(nums) and nums[next]>nums[i]:
                next+=1

            nums[i], nums[next-1] = nums[next-1], nums[i]

            nums[i+1:] = reversed(nums[i+1:])

            return nums

        return nums.sort()