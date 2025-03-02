class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        arr = []
        i1 = i2 = 0

        while i1 < len(nums1) or i2 < len(nums2):
            if i1 < len(nums1):
                id1, val1 = nums1[i1]
            else:
                id1 = inf

            if i2 < len(nums2):
                id2, val2 = nums2[i2]
            else:
                id2 = inf

            if id1 == id2:
                arr.append([id1, val1 + val2])
                i1 += 1
                i2 += 1
            elif id1 > id2:
                arr.append([id2, val2])
                i2 += 1
            else:
                arr.append([id1, val1])
                i1 += 1
        return arr
        