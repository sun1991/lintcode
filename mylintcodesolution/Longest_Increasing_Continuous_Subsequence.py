# http://www.lintcode.com/en/problem/longest-increasing-continuous-subsequence/


class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0

        result1 = self.find(A)
        result2 = self.find(list(reversed(A)))

        return max(result1, result2)

    def find(self, A):
        history_count = max_count = 1
        current_val = A[0]

        for i in range(1, len(A)):
            x = A[i]
            if x > current_val:
                current_val = x
                max_count += 1
            else:
                current_val = x
                history_count = max(max_count, history_count)
                max_count = 1

        return max(max_count, history_count)
    

solution = Solution()
result = solution.longestIncreasingContinuousSubsequence([10])
print(result)















