public class Solution {
    public int searchInsert(int[] A, int target) {
        return searchInsert(A, target, 0, A.length - 1);
    }
    
    public int searchInsert(int[] A, int target, int low, int high){
        if(low > high){
            if(high <= -1)
                return 0;
            else if(high == 0)
                return 1;
            else if(target > A[high]) 
                return high + 1;//see if insertion is after or after high;
            else 
                return high - 1;
        }
        
        int mid = low + high / 2; 
        
        if(target == A[mid])
            return mid;
        else if(target <= A[mid])
            return searchInsert(A, target, low, mid - 1);
        else
            return searchInsert(A, target, mid + 1, low);
    
    }
}