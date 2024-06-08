/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var checkSubarraySum = function(nums, k) {

    const seen = {[nums[0]%k]:0}
    let currSum = nums[0]
    for (let i = 1; i < nums.length; i++ ){
        currSum += nums[i]
        currSum %= k
        if (currSum == 0 || ((currSum in seen) && (i - seen[currSum]) > 1 )) return true
        else if (!(currSum in seen)) seen[currSum] = i
    }
    return false
    
};

// 5 2 4 0 1
// 5 1 5 5 0