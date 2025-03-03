class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        lower = []
        equal = []
        higher = []

        for n in nums:
            if n == pivot:
                equal.append(n)
            elif n < pivot:
                lower.append(n)
            else:
                higher.append(n)
        return lower + equal + higher
        