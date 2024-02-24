class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = []
        for i, n in enumerate(nums):
            total = 1
            for j, n2 in enumerate(nums[:i]):
                if n > n2:
                    total = max(total, dp[j] + 1)
            dp.append(total)
        return max(dp)


        # keep track of min in subsequence
        #
        # if num < min 
        #. update min 


         #. 5.  6.      7       1        8.    9.  ]
        #. (1,1) (2,2). (3, 3). (3,3). (4,5).  (5,6)
         #  

        #  [1 3 2 4 ]. -> 1 2 4
        #. [1 2 2 3]

        #  1      6.     9.   2.     3.     7.     4.     5 -> 1 2 3 4 
        #  (1,1) (2,2) (3,3) (3,3). (3,3). (4, 6) (4, 6). 
        #   1    2.     3.    2.      3.     4.     4

        #  local and running total
        # when hit a lower value, find value last seen (binary search)