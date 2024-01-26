#Bottom-Up aaproach -Tabulation form--dp--O(n*m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]


# top down approach --memorisation-dp--O(2^n)
class Solution:
    def solve(self, i: int, j: int, text1: str, text2: str,dp:List) -> int:
        if i == len(text1) or j == len(text2):
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if text1[i] == text2[j]:
            dp[i][j] = 1 + self.solve(i + 1, j + 1, text1, text2, dp)
        else:
            dp[i][j] = max(self.solve(i, j + 1, text1, text2,dp), self.solve(i + 1, j, text1, text2,dp))
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp =[[-1]*(m+1) for _ in range(n+1)]
        return self.solve(0, 0, text1, text2,dp)

