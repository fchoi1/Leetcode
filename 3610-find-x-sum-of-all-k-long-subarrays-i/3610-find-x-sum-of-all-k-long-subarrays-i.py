class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        ans = []
        N = len(nums)
        for i in range(N-k+1):
            
            count = Counter(nums[i:i+k])

            sorted_count = sorted([(v, k) for k,v in count.items()], reverse=True)[:min(x, len(count))]
            
            ans.append(sum(x[0] * x[1] for x in sorted_count))


        return ans