class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:


        m = len(matrix)
        n = len(matrix[0])
        temp = [[None]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                temp[j][i] = matrix[i][j]

        return temp