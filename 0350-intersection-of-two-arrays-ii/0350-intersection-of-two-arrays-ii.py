class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            nums1Dic = collections.Counter(nums1)
            res = []
            for num in nums2:
                if num in nums1Dic and nums1Dic[num] > 0:
                    res.append(num)
                    nums1Dic[num] -= 1
            return res
        