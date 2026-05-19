class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l = 0
        r = 0

        while l < len(nums1) and r < len(nums2):

            if nums1[l] == nums2[r]:
                return nums1[l]
            

            if nums1[l] > nums2[r]:
                r += 1
            else:
                l += 1

            

        return -1