class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # dp
        counts = [0] * 26
        mod = 10 ** 9 + 7
        for c in s:
            counts[ord(c) - ord('a')] += 1

        for i in range(t):

            curr = counts[0]
            for char in range(1,26):
                temp = counts[char] 
                counts[char] = curr 
                curr = temp
            counts[0] = temp 
            counts[1] += temp


        return sum(counts) % mod