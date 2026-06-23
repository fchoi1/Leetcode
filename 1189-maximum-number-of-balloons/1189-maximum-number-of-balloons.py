class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        ans = inf
        for c in 'ban':
            ans = min(ans, counts[c])
            
        for c in 'lo':
            ans = min(ans, counts[c] // 2)
        
        return ans