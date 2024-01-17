class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr).values()
        unique = set(count)
        return len(unique) == len(count)
        
        