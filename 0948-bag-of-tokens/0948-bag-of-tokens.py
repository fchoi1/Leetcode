class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if not tokens or power < tokens[0]:
            return 0
        lose = score = maxScore = 0
        gain = len(tokens) - 1
        while lose <= gain:
            if  power >= tokens[lose]:
                power -= tokens[lose]
                score += 1
                maxScore = max(maxScore, score)
                lose += 1
            elif score > 0:
                score -= 1
                power += tokens[gain]
                gain -= 1
            else:
                break
                
        return maxScore

        