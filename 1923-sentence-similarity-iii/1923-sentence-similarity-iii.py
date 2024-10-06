class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")
        
        count = 0
        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                count += 1
            else:
                break
                
        for w1, w2 in zip(words1[::-1], words2[::-1]):
            if w1 == w2:
                count += 1
            else:
                break

        return count >= min(len(words1), len(words2))
