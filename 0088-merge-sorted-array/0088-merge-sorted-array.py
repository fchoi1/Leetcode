class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # the m length in nums1 can be used to swap

        i1 = m - 1
        i2 = n - 1
        i = m + n - 1

        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[i] = nums1[i1]
                i1 -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1
            i -= 1

        while i2 >= 0:
            nums1[i] = nums2[i2]
            i -= 1
            i2 -= 1

