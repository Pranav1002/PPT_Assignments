class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        st = str(int(''.join([str(n) for n in digits]))+1)

        return (int(n) for n in st)
