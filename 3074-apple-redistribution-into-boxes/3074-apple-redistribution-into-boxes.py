class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total = sum(apple)
        i = 0
        while total > 0 and i < len(capacity):
            total -= capacity[i]
            i += 1
        return i
        