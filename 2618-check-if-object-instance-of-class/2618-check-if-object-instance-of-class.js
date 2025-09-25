/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if(obj === null || obj === undefined || typeof classFunction !== 'function')
        return false;
    switch (classFunction) {
        case Number:
            return typeof obj == 'number'
        case String:
            return typeof obj == 'string'
        case Boolean:
            return typeof obj == 'boolean'
        case BigInt:
            return typeof obj == 'bigint'
        case Symbol:
            return typeof obj == 'symbol'
        default:
            return Object(obj) instanceof classFunction
    }    
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */