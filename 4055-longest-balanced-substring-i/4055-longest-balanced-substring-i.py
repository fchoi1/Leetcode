class Solution:
    def longestBalanced(self, s: str) -> int:

        # abbbbba
        # brute force + greedy?

        N = len(s)        
        for currLen in range(N, -1, -1):
            counts = Counter(s[:currLen])
  
            for i in range(N - currLen + 1):
                if len(set(counts.values())) <= 1:
                    return currLen
                
                if i + currLen >= N:
                    break

                counts[s[i]] -= 1
                if counts[s[i]] == 0:
                    del counts[s[i]]
                counts[s[i + currLen]] += 1
                
        return 0