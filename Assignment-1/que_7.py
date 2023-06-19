class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        z = 0

        for nz in range(len(nums)):
            if nums[nz]!=0 and nums[z]==0:
                nums[nz], nums[z] = nums[z], nums[nz]

            if nums[z]!=0:
                z+=1