/**
 * @param {number[]} hand
 * @param {number} groupSize
 * @return {boolean}
 */
//  const { MaxPriorityQueue } = require('@datastructures-js/priority-queue');
    
var isNStraightHand = function(hand, groupSize) {
  
    if (hand.length % groupSize !== 0) return false
    const q =  new MinPriorityQueue()
    const map = {}

    hand.forEach((val) => {
        if (!(val in map)) map[val] = 0
        map[val]++
        q.enqueue(val)
    })

    const numsRemove = {}
    while(!q.isEmpty()){

        let curr = q.dequeue().element
        for(let j = 0; j < groupSize; j++) {
            if (!(curr in map) || map[curr] === 0) return false
            else map[curr]--
            if (j !== 0){
                if(!(curr in numsRemove)) numsRemove[curr] = 0
                numsRemove[curr]++
            }
            curr ++
        }
        while(!q.isEmpty() && q.front().element in numsRemove && numsRemove[q.front().element] > 0){
            numsRemove[q.front().element]--
            q.dequeue()
        }
    }


    return true
    
};