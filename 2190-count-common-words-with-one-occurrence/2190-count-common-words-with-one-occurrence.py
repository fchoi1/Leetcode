class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count2 = Counter(words2)
        total = 0
        for w, c in Counter(words1).items():
            if c != 1:
                continue
            if count2[w] == 1:
                total += 1
        
        return total