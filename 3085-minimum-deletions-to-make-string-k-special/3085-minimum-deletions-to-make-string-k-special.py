class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = Counter(word)
        freq = Counter(counts.values())
        sortedFreq = sorted(freq.items())
        left = 0
        right = len(sortedFreq) - 1
        
        steps = inf
        for i, (freq, numFreq) in enumerate(sortedFreq):
            currStep = 0
            for f, nf in sortedFreq[i+1:]:
                if f > (freq + k):
                    currStep += (f - (freq + k)) * nf
         
            for f, nf in sortedFreq[:i]:
                currStep += f * nf
            steps = min(steps, currStep)
            
        return steps
                    
      