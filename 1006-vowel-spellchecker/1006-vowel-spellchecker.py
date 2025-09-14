class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        # lengths
        wordSet = set(wordlist)
        lowerDict = {}
        vowelDict = {}
        ans = []
        for word in wordlist:
            if word.lower() not in lowerDict:
                lowerDict[word.lower()] = word

            vowelWord = ""
            for char in word.lower():
                vowelWord += "*"  if char in "aeiou" else char

            if vowelWord not in vowelDict:
                vowelDict[vowelWord] = word

        for query in queries:
            vowel = ""
            for char in query.lower():
                vowel += "*"  if char in "aeiou" else char
                
            if query in wordSet:
                ans.append(query)
            elif query.lower() in lowerDict:
                ans.append(lowerDict[query.lower()])
            elif vowel in vowelDict:
                ans.append(vowelDict[vowel])
            else:
                ans.append("")
            
        return ans
        