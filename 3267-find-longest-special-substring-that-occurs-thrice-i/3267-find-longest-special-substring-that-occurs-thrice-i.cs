public class Solution {
    public int MaximumLength(string s) {
        int n = s.Length;
        int l = 1, r = n;

        // Call helper function for the initial condition
        if (!Helper(s, n, l)) return -1;

        while (l + 1 < r) {
            int mid = (l + r) / 2;
            if (Helper(s, n, mid)) l = mid;
            else r = mid;
        }

        return l;
    }

    private bool Helper(string s, int n, int x) {
        int[] cnt = new int[26];  // Array to count character frequencies
        int p = 0;

        for (int i = 0; i < n; i++) {
            while (s[p] != s[i]) p++;  // Move p until we find the matching character
            if (i - p + 1 >= x) cnt[s[i] - 'a']++;  // Increment the count for the character
            if (cnt[s[i] - 'a'] > 2) return true;  // If any character appears more than twice, return true
        }

        return false;  // Return false if no character appears more than twice
    }
}