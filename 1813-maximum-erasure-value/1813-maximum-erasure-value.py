class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        slow = curr = score = 0
        unique = set()
        
        for n in nums:
            
            while n in unique:
                unique.remove(nums[slow])
                curr -= nums[slow]
                slow += 1

            unique.add(n)
            curr += n
            score = max(curr, score)
        
        return score

        