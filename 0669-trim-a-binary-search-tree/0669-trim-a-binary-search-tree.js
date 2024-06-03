/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {TreeNode}
 */
 var trimBST = function(root, low, high) {

  function get_next_valid(node){ // 3 | 0 | 2 | 1 | 4
    if (!node) return null

    if (node.val >= low && node.val <= high){ 
      node.left = get_next_valid(node.left) //  left = 0,  | left = 1  |  left = null | left = null
      node.right = get_next_valid(node.right) // right = 4 | right = null | right = null | null = null
      return node; // 1 | 2
    }else if(node.val < low) {
      return get_next_valid(node.right) // right = 2 | (bubble up 2) |
    }else{
      return get_next_valid(node.left)
    }
  }

  return get_next_valid(root) 
    
};