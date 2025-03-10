class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        counts = defaultdict(int)
        vowel_index = defaultdict(int)
        k_queue = deque()

        def isValid(counts):
            for key in 'aeiou':
                if counts[key] <= 0:
                    return False
            return counts['_'] == k

        l = r = c = 0

        while r < len(word):
            char = word[r]
            if char in "aeiou":
                counts[char] += 1
                vowel_index[char] = r
            else:
                counts['_'] += 1
                k_queue.append(r)
            
            
            while counts['_'] > k:
                if word[l] in 'aeuio':
                    counts[word[l]] -= 1
                else:
                    counts['_'] -= 1
                    k_queue.popleft()
                l += 1
            
            # we need left and extended right
            if isValid(counts):
                v_index = min(vowel_index[letter] for letter in 'aeiuo')
                if k == 0:
                    last_index = v_index
                else:
                    last_index = min(v_index, k_queue[0])
                c += last_index - l + 1
            
            r += 1
        return c