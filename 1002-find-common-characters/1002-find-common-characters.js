/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function(words) {
    const wordMap = new Array(26).fill(Infinity);

    for (const word of words){
        const count = new Array(26).fill(0);

        for(const char of word){
            count[char.charCodeAt(0) - 'a'.charCodeAt(0)]++
        }
        for(let i = 0; i < 26; i++){
            wordMap[i] = Math.min(wordMap[i] ,count[i])
        }
    }
    
    const ans = []
    const strMap = 'abcdefghijklmnopqrstuvwxyz'
    for(let i = 0; i < 26; i++){
        if(wordMap[i]) ans.push(...Array(wordMap[i]).fill(strMap[i]))    }
    return ans
    
};