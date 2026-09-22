class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols, rows = len(matrix[0]), len(matrix)
        l, r = 0, cols * rows - 1
        while l <= r:
            m = (l + r) // 2
            num = matrix[m // cols][m % cols]
            if num == target:
                return True
            if num < target:
                l = m + 1
            else:
                r = m - 1
        return False
