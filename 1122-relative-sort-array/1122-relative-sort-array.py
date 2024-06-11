class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr_set = set(arr2)
        counts = Counter(arr1)
        missing = []
        for n in arr1:
            if n not in arr_set:
                missing.append(n)
        res = []
        for n in arr2:
            res += [n] * counts[n]
        return res + sorted(missing)
            
        