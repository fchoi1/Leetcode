class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        largest = -1
        for k,v in counts.items():
            if k == v:
                largest = max(largest, k)

        return largest
        