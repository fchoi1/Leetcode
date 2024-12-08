class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        events.sort()
        heap = []
        ans = -inf
        maxValue = -inf
        # print(events)
        for s,e,val in events:
            # print("ANS", ans, maxValue)
            while heap and s > heap[0][0]:
                _, curr = heappop(heap)
                maxValue = max(maxValue, curr)
            ans = max(ans, maxValue + val)
            heappush(heap, (e, val))
        # print("done", heap, ans, maxValue)
        while heap:
            _, curr = heappop(heap)
            ans = max(ans, curr)
        return ans

        