class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m*n - 1
        
        while(start<=end):
            mid = (start + end)//2

            row = mid//n
            col = mid%n

            if matrix[row][col]==target:
                return True

            if matrix[row][col]<=target:
                start = mid+1

            elif target<matrix[row][col]:
                end = mid-1

        return False