class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        arr = [0 for _ in range(n)]
        arr[0] = 1
        for i in range(n):
            curr = arr[i]
            start = min(n, i + delay)
            end = min(n, i + forget)
            for j in range(start, end):
                arr[j] += curr
        return sum(arr[-forget:]) 
                