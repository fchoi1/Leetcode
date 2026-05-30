import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

class Solution {
    
    // A simple Fenwick Tree (Binary Indexed Tree) to track maximums
    class MaxBIT {
        int[] tree;
        int n;
        
        public MaxBIT(int n) {
            this.n = n;
            tree = new int[n + 1];
        }
        
        // Point update to a larger value
        public void update(int i, int val) {
            for (; i <= n; i += i & -i) {
                tree[i] = Math.max(tree[i], val);
            }
        }
        
        // Query the maximum value up to index i
        public int query(int i) {
            int max = 0;
            for (; i > 0; i -= i & -i) {
                max = Math.max(max, tree[i]);
            }
            return max;
        }
    }

    public List<Boolean> getResults(int[][] queries) {
        int maxX = 0;
        // Find the absolute maximum X to size our Fenwick Tree
        for (int[] q : queries) {
            maxX = Math.max(maxX, q[1]);
        }

        TreeSet<Integer> obstacles = new TreeSet<>();
        obstacles.add(0); // The origin is always an implicit obstacle
        
        // 1. Build the final state of all obstacles
        for (int[] q : queries) {
            if (q[0] == 1) {
                obstacles.add(q[1]);
            }
        }

        MaxBIT bit = new MaxBIT(maxX + 1);
        int prev = 0;
        
        // 2. Initialize the BIT with the gaps of the final state
        for (int x : obstacles) {
            if (x == 0) continue;
            bit.update(x, x - prev);
            prev = x;
        }

        int n = queries.length;
        Boolean[] ans = new Boolean[n]; // Use Boolean array to hold results by index

        // 3. Process queries in reverse
        for (int i = n - 1; i >= 0; i--) {
            int[] q = queries[i];
            int x = q[1];
            
            if (q[0] == 2) { // Query block placement
                int sz = q[2];
                // Max gap fully enclosed before x
                int maxGapInBIT = bit.query(x); 
                
                // Partial gap from the last obstacle up to x
                int lastObs = obstacles.floor(x);
                int currentGap = x - lastObs;
                
                // The answer is true if either the best historical gap, or the current edge gap fits 'sz'
                ans[i] = Math.max(maxGapInBIT, currentGap) >= sz;
            } else { // Remove obstacle (Type 1 in reverse)
                obstacles.remove(x);
                Integer lower = obstacles.floor(x);
                Integer higher = obstacles.ceiling(x);
                
                // Merge the gap and update the BIT at the higher obstacle
                if (higher != null && lower != null) {
                    bit.update(higher, higher - lower);
                }
            }
        }

        // 4. Collect non-null answers in the correct forward order
        List<Boolean> result = new ArrayList<>();
        for (Boolean res : ans) {
            if (res != null) {
                result.add(res);
            }
        }

        return result;
    }
}