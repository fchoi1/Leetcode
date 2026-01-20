class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # check row


        l = 0
        r = len(matrix) - 1

        # 0, 2
        while l < r:
            mid = (l + r) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        row = matrix[l]


        l = 0
        r = len(row) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == row[mid]:
                return True
            elif row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return row[min(l,r)] == target