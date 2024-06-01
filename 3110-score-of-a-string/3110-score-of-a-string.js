/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {

    let score = 0
    let prev = s[0]
    for(char of s){
        score += Math.abs(char.charCodeAt(0) - prev.charCodeAt(0))
        prev = char
    }
    return score
};