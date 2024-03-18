class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        for a,b,x,y in rects:
            if self.weights:
                self.weights.append(((x-a+1)*(y-b+1))+self.weights[-1])
            else:
                self.weights.append((x-a+1)*(y-b+1))

    def pick(self) -> List[int]:
        w = random.randint(0, self.weights[-1])
        l = 0
        r = len(self.weights)-1
        while l < r:
            mid = (r+l)//2  
            if w == self.weights[mid]:
                l = mid
                break
            elif w > self.weights[mid]:
                l = mid + 1
            else:
                r = mid 
        a,b,x,y = self.rects[l]
        newX = random.randint(a,x)
        newY = random.randint(b,y)
        return (newX, newY)


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()