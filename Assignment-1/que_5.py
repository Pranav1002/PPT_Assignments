class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p,q,k = m-1, n-1, m+n-1

        while q>=0:
            if p>=0 and nums1[p]>nums2[q]:
                nums1[k] = nums1[p]
                p-=1
            else:
                nums1[k] = nums2[q]
                q-=1
            k-=1