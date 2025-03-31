class Solution:
    def rankTeams(self, votes: List[str]) -> str:

    
        N = len(votes[0])
        counts = [[0 for _ in range(26)] for _ in range(N)]

        for v in votes:
            for i,c in enumerate(v):
                counts[i][ord(c) - ord('A')] += 1

        for row in counts:
            print(row)
        # organzie into tuples
        sorted_v = []
        for i in range(26):
            sorted_v.append((tuple(counts[j][i] for j in range(N)), -i, chr(65 + i)))
        sorted_v.sort(reverse=True)

        return "".join([char for _,_,char in sorted_v[:N]])

        