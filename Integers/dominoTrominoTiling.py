class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7 # to prevent overflow and to return the result modulo 10^9 + 7
        
        if n <= 2:
            return n
        
        a, b, c = 1, 1, 2  # dp[0], dp[1], dp[2]
        
        for i in range(3, n + 1):
            d = (2 * c + a) % MOD # dp[i] = 2*dp[i-1] + dp[i-3]
            a, b, c = b, c, d
        
        return c