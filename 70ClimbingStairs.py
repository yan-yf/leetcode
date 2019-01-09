class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # fibonacci
        # dp[n] = dp[n-1] + dp[n-2]
        dp = [1 for _ in range(n+1)]
        for x in range(2, n+1):
        	dp[x] = dp[x-1] + dp[x-2]
        return dp[n]
