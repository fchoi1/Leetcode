/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    
    nums.sort((a,b) => a-b)
    let arr2, arr3;
    let target2, target3, n, l=0, r=0;
    let ans = {};
    //console.log(nums)
    if(nums.length < 4) return []
    for(let i = 0; i < nums.length; i++){
        target2 = target - nums[i];
        arr2 = nums.slice(i+1, nums.length)
        // console.log(arr2, i)
        for(let j = 0; j < arr2.length; j++){
            target3 = target2 - arr2[j]
            arr3 = arr2.slice(j+1, arr2.length)
            l = 0;
            r = 0;
            //console.log(arr3, target3, nums[i], arr2[j])
            for(let k = 0; k < arr3.length-1; k++){
                // console.log(l,arr3.length - r - 1)
                // console.log('target', target3,  'left',  arr3[l], 'right', arr3[arr3.length - r - 1] )

                if((target3 - arr3[l]) > arr3[arr3.length - r - 1]){
                    l++
                }else if((target3 - arr3[l]) < arr3[arr3.length - r - 1]){
                    r++
                }else if((target3 - arr3[l]) == arr3[arr3.length - r - 1]){
                    n = String(nums[i]) + String(arr2[j]) + String(arr3[l]) + String(arr3[arr3.length-r-1])
                    //console.log('match;', [nums[i], arr2[j], arr3[l], arr3[arr3.length-r-1]])
                    ans[n] = [nums[i], arr2[j], arr3[l], arr3[arr3.length-r-1]]
                    l++
                }
                if(l == arr3.length - r - 1) break;
            }
        }
    }
    //console.log(ans)
    return Object.values(ans)
};