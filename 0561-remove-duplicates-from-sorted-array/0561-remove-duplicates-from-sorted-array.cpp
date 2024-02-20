class Solution {
public:
    int removeDuplicates(int A[], int n) {
        int i,length = 0;
        A[length++] = A[0]
        for(i = 1;i<n;i++ ){
            if(A[i] == A[length-1]) i++;
            else A[length++] = A[i]
        }
        
        return length
    }
};