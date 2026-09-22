class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l < r:
            m1 = (l + r) // 2
            
            if target < matrix[m1 + 1][0]:
                if matrix[m1][0] <= target:
                    r = m1
                    break
                r = m1 - 1
        
            else:
                l = m1 + 1
        m1 = r

        l, r = 0, len(matrix[m1]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m1][m] == target:
                return True
            if matrix[m1][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
