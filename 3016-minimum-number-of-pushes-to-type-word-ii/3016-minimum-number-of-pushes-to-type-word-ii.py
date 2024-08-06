class Solution:
    def minimumPushes(self, word: str) -> int:
        letters = [0] * 26
        for char in word:
            letters[ord(char) - ord('a')] += 1

        letters.sort(reverse=True)
        pushes = 0
        buttons = 0
        for c in letters:
            pushes += c * (buttons // 8 + 1)
            buttons += 1
            if not c:
                return pushes

        return pushes
        