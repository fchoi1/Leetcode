class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        max_gain = 0
        for g in gain:
            curr += g
            max_gain = max(max_gain, curr)
        return max_gain