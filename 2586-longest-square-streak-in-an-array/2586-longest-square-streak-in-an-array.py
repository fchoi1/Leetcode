class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # get longest subsequence of sqaures first?

        # 300 max

        unique = set(nums)
        squares = []
        for n in unique:
            if sqrt(n) == int(sqrt(n)):
                squares.append(n)
        ans = 0
        s = set(squares)
        for n in unique:
            c = 1
            while n**2 in s:
                c += 1
                n = n ** 2
            ans = max(c, ans)
        
        return - 1 if ans <= 1 else ans
                