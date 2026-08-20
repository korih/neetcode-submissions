class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            m_val = matrix[m][0]

            if m_val == target:
                return True
            if target < m_val:
                r = m - 1
                continue
            if m_val < target:
                l = m + 1
                continue
        
        if l - 1 < 0:
            return False

        l2 = 0
        r2 = len(matrix[l - 1]) - 1
        while l2 <= r2:
            m = (l2 + r2) // 2
            m_val = matrix[l - 1][m]
            if m_val == target:
                return True
            if target < m_val:
                r2 = m - 1
            else:
                l2 = m + 1
        
        return False