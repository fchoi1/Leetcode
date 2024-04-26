class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        # lengths
        wordSet = set()
        lowerDict = {}
        vowelDict = {}
        ans = []
        for i,word in enumerate(wordlist):
            if word.lower() not in lowerDict:
                lowerDict[word.lower()] = i
            wordSet.add(word)

            vowelWord = ""
            for char in word.lower():
                vowelWord += "*"  if char in "aeiou" else char

            if vowelWord not in vowelDict:
                vowelDict[vowelWord] = i

          
        
        for query in queries:
            vowel = ""
            for char in query.lower():
                vowel += "*"  if char in "aeiou" else char
                
            if query in wordSet:
                ans.append(query)
            elif query.lower() in lowerDict:
                ans.append(wordlist[lowerDict[query.lower()]])
            elif vowel in vowelDict:
                ans.append(wordlist[vowelDict[vowel]])
            else:
                ans.append("")
            
        return ans
        