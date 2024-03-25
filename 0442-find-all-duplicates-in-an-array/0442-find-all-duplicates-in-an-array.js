/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
  dupes = []
  
  dupes = nums.filter((number,i) => {
    if(nums[Math.abs(number)-1] > 0){
      nums[Math.abs(number)-1] *= -1
      return false
    }else{
      return true
    }
  }).map(el => Math.abs(el));
    
  return dupes
};