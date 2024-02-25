public class Solution {
    public int minCut(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        
        int[] cut = new int[s.length() + 1];
        boolean[][] isPalindrome = getIsPalindrome(s);
        
        cut[0] = 0;
        for (int i = 1; i <= s.length(); i++) {
            cut[i] = Integer.MAX_VALUE;
            //j is the length of a substring
            for (int j = 1; j <= i; j++) {
                if (isPalindrome[i - j][i - 1] && cut[i - j] != Integer.MAX_VALUE) {
                    cut[i] = Math.min(cut[i], cut[i - j] + 1);
                }
            }
        }
        
        return cut[s.length()] - 1;
    }
    
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    
    public boolean[][] getIsPalindrome(String s) {
        boolean[][] result = new boolean[s.length()][s.length()]();
        
        for (int i = 0; i < s.length(); i++) {
            result[i][i] = true;
        }
        
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j < s.length(); j++) {
                result[i][j] = isPalindrome(s.substring(i,j+1));
            }
        }
        return result;
    }
}