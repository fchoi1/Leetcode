class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        s = ""

        heap =[(-count, letter) for letter, count in c.items()]
        heapify(heap)
        prev = None

        while heap and len(heap) > 0:
            count, letter = heappop(heap)
            if prev:
                heappush(heap, prev)
            s += letter
            count += 1
            if count != 0:
                prev = (count, letter)
            else:
                prev = None

        if heap and -heap[0][0] > 0 or prev and -prev[0] > 0:
            return ""
        return s


        