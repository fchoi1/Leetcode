class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # sortting
        # but only 
    
        def getLowest(nums):
            a = b = c =  float('inf')
            for val in nums:
                if val < a:
                    c = b
                    b = a
                    a = val
                elif val < b:
                    c = b
                    b = val
                elif val < c:
                    c = val
            return a,b,c

        a,b,c = getLowest(nums1)
        min2 = min(nums2)
        minX = float('inf')
        n1Set = Counter(nums1)
        for val in [min2 - a, min2 - b, min2 - c]:
            counts = defaultdict(int)
            for n2 in nums2:
                if n2 - val not in n1Set:
                    break
                counts[n2 - val] += 1
                if counts[n2 - val] > n1Set[n2-val]:
                    break
            else:
                minX = min(minX, val)
    
        return minX
                
