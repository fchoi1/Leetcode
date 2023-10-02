import heapq
from math import floor, sqrt
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            currMax = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(currMax)))
        return sum(-x for x in gifts)