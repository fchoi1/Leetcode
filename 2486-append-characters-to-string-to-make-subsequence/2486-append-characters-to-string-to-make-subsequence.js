/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var appendCharacters = function(s, t) {
    // greedy?
    let t_index = 0

    for (const char of s){
        if (char === t[t_index]) {
            t_index ++}
        if (t_index >= t.length) return 0
    }
    return t.length - t_index
    
};