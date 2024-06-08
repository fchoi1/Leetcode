/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var checkSubarraySum = function(nums, k) {
    if (nums.length < 2) return false
    const seen = {0:-1}
    let currSum = 0
    for (let i = 0; i < nums.length; i++ ){
        currSum = (currSum + nums[i]) % k
        if ((currSum in seen) && (i - seen[currSum]) > 1 ) return true
        else if (!(currSum in seen)) seen[currSum] = i
    }
    return false
    
};

// 5 2 4 0 1
// 5 1 5 5 0