var subarraysDivByK = function(nums, k) {
    const counts = {0: 1}
    let currSum = 0, ans = 0
    nums.forEach(val => {
        currSum = (currSum + val) % k
        if (currSum < 0) currSum += k
        if (currSum in counts) ans += counts[currSum]
        else counts[currSum] = 0
        counts[currSum] ++
    })
    return ans
};