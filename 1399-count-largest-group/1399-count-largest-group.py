class Solution:
    def countLargestGroup(self, n: int) -> int:

        arr = [0] * 36

        for i in range(1, n+1):
            s = sum(int(x) for x in str(i))
            arr[s-1] += 1
        
        m = max(arr)
        return sum(x == m for x in arr)