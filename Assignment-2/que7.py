class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        inc,dec = True, True

        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                inc = False

            elif nums[i]<nums[i+1]:
                dec = False

        return inc or dec
    