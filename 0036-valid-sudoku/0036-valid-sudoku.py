class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def hasDuplicate(arr):
            seen = set()
            for n in arr:
                if n in seen:
                    return True
                seen.add(n)
            return False

        for i in range(9):
            # row
            row = board[i]
            if hasDuplicate(list(filter(lambda x: x != '.', row))):
                return False
            
            # col
            col = [r[i] for r in board]
            if hasDuplicate(list(filter(lambda x: x != '.', col))):
                return False

            # box
            box_x = (i * 3) % 9
            box_y = i // 3 * 3
            box = []
            for x in range(3):
                for y in range(3):
                    val = board[box_y + y][box_x + x]
                    if val != '.':
                        box.append(val)
            if hasDuplicate(list(filter(lambda x: x != '.', box))):
                return False

        return True
        # col
        # box
        