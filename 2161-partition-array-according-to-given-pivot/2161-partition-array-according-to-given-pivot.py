class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low = []
        high = []
        same = []

        for n in nums:
            if n == pivot:
                same.append(n)
            elif n < pivot:
                low.append(n)
            else:
                high.append(n)

        return low + same + high

