class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        dic = {}

        dic = {0:-1}
        s=0
        ans=0
        for i in range(len(nums)):

            if nums[i]==0:
                s+=-1

            elif nums[i]==1:
                s+=1

            try:
                ln = i - dic[s]
                if ln>ans:
                    ans=ln
            except:
                dic[s]=i

        return ans
