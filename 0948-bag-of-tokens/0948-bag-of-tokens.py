class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if not tokens or power < tokens[0]:
            return 0
        lose = score = 0
        gain = len(tokens) - 1
        while lose <= gain:
            while lose < len(tokens) and power >= tokens[lose]:
                power -= tokens[lose]
                score += 1
                lose += 1

            if lose >= gain:
                break
                
            if score > 0:
                score -= 1
                power += tokens[gain]
                gain -= 1
                
        return score

        