class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        sorted_times = sorted(enumerate(times), key=lambda x: x[1])
        avail = list(range(len(times)))
        heap = []
        for i, (start, end) in sorted_times:
            while heap and start >= heap[0][0]:
                _, seat = heapq.heappop(heap)
                heapq.heappush(avail, seat)
            next_seat = heapq.heappop(avail)
            heapq.heappush(heap, (end,next_seat))
            if i == targetFriend:
                return next_seat
        return -1
        