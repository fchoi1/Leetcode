class Solution {
public:
    void nextPermutation(vector<int> &num) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int  IDX = num.size () - 1;
        BOOL  InOrder = true ;
        while  (IDX> 0) {
            IF  ((num [IDX]> num [IDX-1])) {
                InOrder = false ;
                break ;
            }
            idx -;
        }   
        IF  (InOrder) {
            sort (num.begin (), num.end ());
            return ;
        }
        idx -;
        / / Idx is the number need to be exchanged
        int  Minidx = INT_MAX;
        for  ( int  i = IDX +1; i <num.size (); i + +) {
            IF  (num [i]> num [IDX]) {
                IF  (Minidx == INT_MAX | | num [i] <num [Minidx])
                {
                    minIdx = i;
                }
            }
        }
        swap (num, idx, minIdx);
        sort (num.begin () + idx + 1, num.end ());
    }
     
    void  swap (Vector < int > & num, int  a, int  b) {
        int  tmp = num [a];
        num [a] = num [b];
        num [b] = tmp;
    }
    }
};