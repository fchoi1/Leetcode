class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1, 1]
        for _ in range(rowIndex-1):
            newRow = [1]
            for a,b in zip(row, row[1:]):
                newRow.append(a+b)
            newRow.append(1)
            row = newRow
        return row