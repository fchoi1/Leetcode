class Robot:

    def __init__(self, width: int, height: int):
        self.length = 2 * (width - 1) + 2 * height - 1
        self.currStep = 0

        self.map = {0: (0,0,'South')}
        
        idx = 1
        for i in range(1, width):
            self.map[idx] = (i, 0, 'East')
            idx += 1

        for i in range(1, height):
            self.map[idx] = (width - 1, i, 'North')
            idx += 1

        for i in range(width - 2, -1, -1):
            self.map[idx] = (i, height - 1, 'West')
            idx += 1

        for i in range(height - 2, -1, -1):
            self.map[idx] = (0, i, 'South')
            idx += 1


    def step(self, num: int) -> None:
        self.currStep += num

    def getPos(self) -> List[int]:
        x,y,_ = self.map[self.currStep % (self.length - 1)]
        return (x, y)
        
    def getDir(self) -> str:
        if self.currStep == 0:
            return 'East'

        return self.map[self.currStep % (self.length - 1)][2]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()