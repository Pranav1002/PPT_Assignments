class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        ans = 0
        
        for num, freq in counter.items():
            if num + 1 in counter:
                ans = max(ans, freq + counter[num + 1])
        
        return ans