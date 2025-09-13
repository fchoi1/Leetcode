class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = Counter(s)
        vowels = 'aeiou'

        max_vowel = max((freq for ch, freq in counts.items() if ch in vowels), default=0)
        max_consonant = max((freq for ch, freq in counts.items() if ch not in vowels), default=0)

        return max_vowel + max_consonant  