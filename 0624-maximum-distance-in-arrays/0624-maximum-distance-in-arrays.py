class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min1 = min2 = (inf, None)
        max1 = max2 = (-inf, None)

        for i,array in enumerate(arrays):
            if array[0] < min1[0]:
                min2 = min1
                min1 = (array[0], i)
            elif array[0] < min2[0]:
                min2 = (array[0], i)

            if array[-1] > max1[0]:
                max2 = max1
                max1 = (array[-1], i)
            elif array[-1] > max2[0]:
                max2 = (array[-1], i)
        
        if max1[1] == min1[1]:
            return max(max1[0] - min2[0],  max2[0] - min1[0])
        return max1[0] - min1[0]
            
        