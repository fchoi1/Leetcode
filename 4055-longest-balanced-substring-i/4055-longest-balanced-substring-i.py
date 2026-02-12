class Solution:
    def longestBalanced(self, s: str) -> int:

        # abbbbba
        # brute force + greedy?

        N = len(s)

        # start at lenght N to 0
        
        for currLen in range(N, -1, -1):
            counts = Counter(s[:currLen])
            print("curr", currLen, counts)
            if len(set(counts.values())) <= 1:
                print('done', counts)
                return currLen

            for i in range(N - currLen):
                counts[s[i]] -= 1
                if counts[s[i]] == 0:
                    del counts[s[i]]
                counts[s[i + currLen]] += 1
                
                if len(set(counts.values())) <= 1:
                    print('done', counts, "loop", i)
                    return currLen
        return 0