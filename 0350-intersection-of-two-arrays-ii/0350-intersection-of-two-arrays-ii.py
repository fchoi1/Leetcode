class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        res = []
        for n in count2:    
            if n in count1:
                res.extend([n] * min(count1[n], count2[n]))
        return res    