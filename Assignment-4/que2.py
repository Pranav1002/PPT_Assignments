class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        x = []
        y = []

        nums1 = set(nums1)
        nums2 = set(nums2)

        for i in nums1:
            if i not in nums2:
                # if nums1[i] not in x:
                    x.append(i)

        for i in nums2:

            if i not in nums1:
                # if nums2[i] not in y:
                    y.append(i)

        return [x,y]