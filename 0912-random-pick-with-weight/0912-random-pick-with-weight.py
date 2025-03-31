import random
class Solution:

    def __init__(self, w: List[int]):

        total = sum(w)
        self.prob = [weight/total for weight in w]
        self.index = list(range(len(w)))

    def pickIndex(self) -> int:
        return random.choices(self.index, weights=self.prob)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()