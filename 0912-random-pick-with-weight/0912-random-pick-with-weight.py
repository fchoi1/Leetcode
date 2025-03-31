import random
class Solution:

    def __init__(self, w: List[int]):

        curr = 0
        self.prob = []
        for weight in w:
            curr += weight
            self.prob.append(curr)
        
        self.total = self.prob[-1]

    def pickIndex(self) -> int:
        i = random.randint(1, self.total)

        l = 0
        r = len(self.prob) - 1
        mid = 0
        while l < r:
            mid = (l + r) // 2
            if i == self.prob[mid]:
                return mid
            if i > self.prob[mid]:
                l = mid + 1
            else:
                r = mid 
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()