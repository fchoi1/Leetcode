class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        sortedScores = sorted(score, reverse=True)
        place = ["Bronze Medal","Silver Medal", "Gold Medal"]
        scoreMap = {}
        for i, val in enumerate(sortedScores):
            if place:
                scoreMap[val] = place[-1]
                place.pop()
            else:
                scoreMap[val] = str(i+1)
        return [scoreMap[val] for val in score]