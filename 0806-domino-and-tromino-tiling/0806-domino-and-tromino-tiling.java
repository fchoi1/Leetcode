class Solution {
    public int numTilings(int n) {
        if(n == 1){
            return 1;
        }
        int[] series = new int[n + 1];
        int mod = 1000000007;
        series[0] = 1;
        series[1] = 1;
        series[2] = 2;

        for(int i=3; i<=n; i++){
            series[i] = ((2*series[i-1])%mod + series[i-3])%mod;
        }
        return series[n];
    }
}