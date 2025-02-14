
var ProductOfNumbers = function() {
    this.arr = [1];
    
};

/** 
 * @param {number} num
 * @return {void}
 */
ProductOfNumbers.prototype.add = function(num) {
    num == 0 ? this.arr = [1] : this.arr.push(num*this.arr[this.arr.length-1])
};

/** 
 * @param {number} k
 * @return {number}
 */
ProductOfNumbers.prototype.getProduct = function(k) {
   return  k >= this.arr.length ? 0 : Math.floor(this.arr[this.arr.length-1]/this.arr[this.arr.length-1-k]);
};

/** 
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = new ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */