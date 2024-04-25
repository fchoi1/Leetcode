class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        heap = []
        for i, char in enumerate(s):
            maxLen = 1
            temp = []
            if heap:
                while heap and abs(ord(heap[0][1]) - ord(char)) > k:
                    temp.append(heapq.heappop(heap))
                maxLen = -heap[0][0] + 1 if heap else 1

            heapq.heappush(heap,(-maxLen,char))
            for val in temp:
                heapq.heappush(heap, val)

        return -heap[0][0]