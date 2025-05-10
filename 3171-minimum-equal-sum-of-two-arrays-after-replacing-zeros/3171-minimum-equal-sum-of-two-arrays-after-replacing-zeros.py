class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = nums1.count(0)
        z2 = nums2.count(0)

        sum1 = sum(nums1)
        sum2 = sum(nums2)

        min2 = sum2 + z2
        min1 = sum1 + z1

        if (z1 == 0 and min2 > min1) or (z2 == 0 and min1 > min2):
            return -1
            
        return max(min1, min2)