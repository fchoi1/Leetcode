class Solution:
    def numTeams(self, rating: List[int]) -> int:
        total = 0
        N = len(rating)
        for i, curr in enumerate(rating):
            # less than
            less = more = 0
            for left in rating[:i]:
                if left < curr:
                    less += 1

            for right in rating[i+1:]:
                if right > curr:
                    more += 1
            total += less * more + (i - less) * (N - i - 1 - more)
            # print(less, more,(i - less), (N - i - 1 - more), total)
        return total


            
        