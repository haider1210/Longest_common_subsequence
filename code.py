#Brute force 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs_recursive(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + lcs_recursive(i + 1, j + 1)
            else:
                return max(lcs_recursive(i + 1, j), lcs_recursive(i, j + 1))

        return lcs_recursive(0, 0)


##
