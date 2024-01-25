class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        data = list(zip([-count for count in counter.values()], counter.keys()))
        heapq.heapify(data)
        string = ""
        prev = None
        while data or prev:
            if data:
                freq, letter = heapq.heappop(data)
            if string and letter == string[-1]:
                return ""
            string += letter
            freq += 1

            if prev and prev[0] != 0:
                heapq.heappush(data, prev)
                prev = None

            if freq != 0:
                prev = (freq, letter)
        return string
                


