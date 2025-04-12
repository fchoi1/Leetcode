#define ll long long

class Solution {
    ll vectorToNumber(vector<int>& num) {
        ll ans = 0;
        for (int digit : num) {
            ans = ans * 10 + digit;
        }
        return ans;
    }

    ll fact(int n){
        ll ans = 1;
        for(int i=2 ; i<=n ; i++) ans *= i;
        return ans;
    }

    ll Total_Permutations(map<int, int> &freq, int n) {
        ll totalPermutations = fact(n);

        for (auto i : freq) {
            totalPermutations /= fact(i.second);
        }
        return totalPermutations;
    }

    // Function to calculate permutations starting with zero
    ll PermutationsStartingWithZero(map<int, int> freq, int n) {
        if (freq.find(0) == freq.end() || freq[0] == 0) {     // When there's no zero 
            return 0;
        }

        freq[0]--;              // Fix one zero as the first digit
        ll permutationsWithZero = fact(n-1);

        for (auto& i : freq) {
            permutationsWithZero /= fact(i.second);
        }
        return permutationsWithZero;
    }

    ll calc(map<int,int> &freq, int n){
        ll a = Total_Permutations(freq,n), b = PermutationsStartingWithZero(freq,n);
        return a - b ;      // Permutations that doesnt start with 0
    }

public:
    ll ans = 0;
    set<map<int,int>> vis;

    void generatePalindrome(vector<int>& num, int left, int right, int k, int n) {
        if (left > right) {
            ll pali = vectorToNumber(num);

            if (pali % k == 0 ) {
                map<int,int>m;

                while(pali){
                    m[pali%10]++;
                    pali /= 10;
                }
                
                if(vis.find(m) == vis.end()){
                    ans += calc(m,n);
                    vis.insert(m);
                }
            }
            return;
        }

        // Set the current digit to all possible values from 0 to 9
        for (int digit = (left == 0) ? 1 : 0; digit <= 9; ++digit) {
            num[left] = num[right] = digit;
            generatePalindrome(num, left + 1, right - 1, k, n);
        }
    }

    ll countGoodIntegers(int n, int k) {
        vector<int> num(n);
        generatePalindrome(num, 0, n-1, k, n);
        return ans;
    }
};