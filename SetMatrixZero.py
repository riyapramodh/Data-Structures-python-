#if zero is found in a particular position say mat[i][j] then that entire row and column trailing the zero will be set to 0.
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(m))  # Should iterate up to m, not n
        first_col_zero = any(matrix[i][0] == 0 for i in range(n))

        # Mark rows and columns to be zeroed
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Apply zeroing based on markings
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out first row and column if needed
        if first_row_zero:
            for j in range(m):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(n):
                matrix[i][0] = 0
