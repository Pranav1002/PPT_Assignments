class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n = len(nums)
        nums.sort()
        diff = 20001
        ans = 0

        for i in range(n-2):
            a = i+1
            b = n-1
            s = 0
            while(a<b):
                s = nums[a]+ nums[b]+ nums[i]

                if s==target:
                    return s

                elif abs(s-target)<diff:
                    diff=abs(s-target)
                    ans = s
                
                if s>target:
                    b-=1
                else:
                    a+=1
        return ans
