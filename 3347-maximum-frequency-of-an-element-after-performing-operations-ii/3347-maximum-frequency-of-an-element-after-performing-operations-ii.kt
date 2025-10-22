class Solution {
    fun maxFrequency(nums: IntArray, k: Int, numOperations: Int): Int {
        val mx = nums.max()
        val n = mx + k + 2
        val f = IntArray(n)
        for (x in nums) f[x]++
        val pre = IntArray(n)
        pre[0] = f[0]
        for (i in 1 until n) pre[i] = pre[i - 1] + f[i]
        var ans = 0
        for (t in 0 until n) {
            if (f[t] == 0 && numOperations == 0) continue
            val l = maxOf(0, t - k)
            val r = minOf(n - 1, t + k)
            val tot = pre[r] - if (l > 0) pre[l - 1] else 0
            val adj = tot - f[t]
            val value = f[t] + minOf(numOperations, adj)
            ans = maxOf(ans, value)
        }
        return ans
    }
}