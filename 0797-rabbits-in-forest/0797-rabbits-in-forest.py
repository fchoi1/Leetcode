class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = defaultdict(int)
        rabbits = 0

        for n in answers:
            if n not in counts:
                counts[n] = 0
            else:
                counts[n] += 1
                if counts[n] > n:
                    rabbits += n + 1
                    counts[n] = 0
                    
        for k, n in counts.items():
            rabbits += k + 1
        return rabbits
                
        