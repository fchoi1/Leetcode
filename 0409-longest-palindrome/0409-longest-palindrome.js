/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {

    const charMap = new Set()
    let count = 0
    for (const char of s){
        if(!charMap.has(char)) charMap.add(char)
        else {
            count += 2
            charMap.delete(char)
            }
    }
    return count + (charMap.size > 0 ? 1 : 0)
};