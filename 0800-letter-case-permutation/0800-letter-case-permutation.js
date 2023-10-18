/**
 * @param {string} s
 * @return {string[]}
 */
var letterCasePermutation = function(s) {
    const res = []
    const generate = (string, i) =>{
        if (i == s.length){
            res.push(string)
            return            
        }

        if (!isNaN(parseInt(s[i]))){
            generate(string + s[i], i+1)
        }else{
            generate(string + s[i].toUpperCase(), i+1)
            generate(string + s[i].toLowerCase(), i+1)
        }
    }
    generate("", 0)
    return res
    
};