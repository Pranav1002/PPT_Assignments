class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        st=""
        ans=[]
        count=0

        for i in range(len(nums)):

            if i+1<len(nums) and nums[i+1] == nums[i]+1:
                count+=1
                continue

            if count>0:
                st = str(nums[i-count])+"->"+str(nums[i])
                count=0

            else:
                st = str(nums[i])
            
            ans.append(st)

        return ans