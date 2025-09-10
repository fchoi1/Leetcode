class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        arr = []
        for n in nums:
            curr += n
            
            arr.append(curr)

        seen = defaultdict(int)
        seen[0] = 1
        counts = 0
        for n in arr:
            diff = n - k
            # print('add diff', diff, seen[diff])
            counts += seen[diff]
            seen[n] += 1
        
        print(counts, seen)
        return counts