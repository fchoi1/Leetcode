/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    functions.reverse()

	return function(x) {
        let res = x
        // console.log('x', x)
        
        functions.forEach(f => {
            res = f(res)
            // console.log(res)
        })
    return res
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */