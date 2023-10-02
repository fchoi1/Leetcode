class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        p1 = p2 = 0
        result = []
        while p1 < len(nums1) and p2 < len(nums2):

            id1, id2 = nums1[p1][0], nums2[p2][0]
            val1, val2 = nums1[p1][1], nums2[p2][1]

            if id1 == id2:
                result.append([id1, val1 + val2])
                p1 += 1
                p2 += 1
            elif id1 > id2:
                result.append([id2, val2])
                p2 += 1
            elif id1 < id2:
                result.append([id1, val1])
                p1 += 1
        print(p1, len(nums1), p2, len(nums2),)

        if p1 >= len(nums1) and p2 < len(nums2):
            result.extend(nums2[p2:]) 
        if p2 >= len(nums2) and p1 < len(nums1):
            result.extend(nums1[p1:]) 
        return result

        