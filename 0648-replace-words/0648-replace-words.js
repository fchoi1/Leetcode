/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */
var replaceWords = function(dictionary, sentence) {
    const root = new Trie(null)
    

    dictionary.forEach((word) => {
        let curr = root
        for (const char of word){
            if (!curr[char]) curr[char] = new Trie(char)
            curr = curr[char]
        }
        if (!curr.end){
            curr.end = true
            curr.word = word
        }
    })

    let new_string
    sentence.split(' ').forEach(word => {
        let curr = root
        let new_word 
        for (const char of word){
            if (!curr[char]) {
                new_word = word
                break
            }else if (curr[char].end){
                new_word = curr[char].word
                break
            }
            curr = curr[char]
        }
        if (new_string) new_string += ` ${new_word}`
        else new_string = new_word
        
    })
    return new_string
};

class Trie{
    constructor(val, end=false, word=''){
        this.val = val
        this.end = end
        this.word = word
        this.neighbors = {}
    }
}