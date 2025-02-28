class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # search  row

        # search col

        mid = l = 0
        r = len(matrix) - 1
        while l < r:
            mid = (l + r) // 2
            print(mid, r, l, target, matrix[mid])
            if matrix[mid][0] == target:
                return True
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l = mid
                break
            
            if target > matrix[mid][0]:
                l = mid + 1
            else:
                r = mid - 1
            print('chec', l, mid, r, target, matrix[mid][0])
     
        
        row = matrix[l]
        l = 0
        r = len(row)
        print("brok", row, l ,r, mid)
        while l < r:
            mid = (l + r) //  2
            if row[mid] == target:
                return True
            if target > row[mid]:
                l = mid + 1
            else:
                r = mid 
        return False