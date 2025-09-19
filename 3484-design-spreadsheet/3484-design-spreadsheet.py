class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = defaultdict(int) # A1, etc
        

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value
        

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0
        

    def getValue(self, formula: str) -> int:
        _, X, Y = re.split(r'=|\+', formula)
        if X.isnumeric():
            X_val = int(X) 
        else:
            X_val = self.cells[X]

        if Y.isnumeric():
            Y_val = int(Y) 
        else:
            Y_val = self.cells[Y]


        return X_val + Y_val


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)