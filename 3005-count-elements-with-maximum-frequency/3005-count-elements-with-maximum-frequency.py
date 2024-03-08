class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = 0
        freq = defaultdict(int)
        maxFreq = 1
        for n in nums:
            freq[n] += 1
            if freq[n] > maxFreq:
                count = 1
                maxFreq = freq[n]
            elif maxFreq == freq[n]:
                count += 1
        return count * maxFreq
        