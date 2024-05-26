class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def get_pairs(n, counts):
            pairs = 0
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    if i in counts:
                        pairs += counts[i]
                    if i != n // i:
                        if n // i in counts:
                            pairs += counts[n//i]
            return pairs
        
        div = []
        pairs = 0
        # cache ? 
        for n in nums1:
            if n / k == n // k:
                div.append(n//k)
                
        counts = Counter(nums2)
        for val in div:
            pairs += get_pairs(val, counts)
         
        return pairs
        
        #