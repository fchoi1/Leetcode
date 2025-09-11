class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'AEIOUaeiou'
        # upper to lower

        idx = 0

        counts = Counter(s)     

        new_s = ''

        for char in s:
            if char not in vowels:
                new_s += char
            else:
                while counts[vowels[idx]] == 0:
                    idx += 1
                new_s += vowels[idx]
                counts[vowels[idx]] -= 1

        return new_s