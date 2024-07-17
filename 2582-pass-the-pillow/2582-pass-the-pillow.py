class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        loop = (n - 1) * 2 # 6
        remain = time % loop + 1 # 5  
        # print(remain) 
        return remain if remain < n else 2*n - remain
        