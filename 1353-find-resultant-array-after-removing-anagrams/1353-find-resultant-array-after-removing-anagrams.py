class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        remove = []

        while True:
            remove = False
            temp = [words[0]]
            for prev, curr in zip(words[:], words[1:]):
                if Counter(prev) == Counter(curr):
                    continue
                    remove = True
                else:
                    temp.append(curr)

            words = temp
            if not remove:
                break
        return words