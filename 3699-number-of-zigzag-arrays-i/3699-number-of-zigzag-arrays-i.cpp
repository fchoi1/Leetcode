class Solution {
public:
    long long MOD = 1e9 + 7;
    int zigZagArrays(int n, int l, int r) 
    {
        int m = r - l + 1;
        if (n == 1) {
            return m;
        }
        vector<long long> up(m + 1, 0);
        vector<long long> down(m + 1, 0);
        for (int j = 1; j <= m; j++) 
        {
            up[j] = j - 1;
            down[j] = m - j;
        }
        vector<long long> prefix_up(m + 1, 0);
        vector<long long> prefix_down(m + 1, 0);
        vector<long long> next_up(m + 1, 0);
        vector<long long> next_down(m + 1, 0);
        for (int len = 3; len <= n; len++) 
        {
            for (int i = 1; i <= m; i++) 
            {
                prefix_up[i] = (prefix_up[i - 1] + up[i]) % MOD;
                prefix_down[i] = (prefix_down[i - 1] + down[i]) % MOD;
            }
            for (int j = 1; j <= m; j++) 
            {
                next_up[j] = prefix_down[j - 1];
                next_down[j] = (prefix_up[m] - prefix_up[j] + MOD) % MOD;
            }
            up = next_up;
            down = next_down;
        }
        long long ans = 0;
        for (int j = 1; j <= m; j++) {
            ans = (ans + up[j] + down[j]) % MOD;
        }
        return (int)ans;
    }
};