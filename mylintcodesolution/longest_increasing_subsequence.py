# http://www.lintcode.com/en/problem/longest-increasing-subsequence/


#For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
#For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4
import copy
class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0

        self.data = nums
        self.result_dict = {}

        self.find_result()

        return len(self.result_dict)

    def find_result(self):
        for x in self.data:
            subseq = self.find_subsequence(x)
            self.result_dict[len(subseq)] = subseq

        return max(self.result_dict.keys())

    def find_subsequence(self, x):
        for key in range(len(self.result_dict), 0, -1):
            row = self.result_dict[key]
            if row[-1] < x:
                tmprow = copy.copy(row)
                tmprow.append(x)
                return tmprow
        else:
            return [x]



test_data = [4, 2, 4, 5, 3, 7]
solution = Solution()
result = solution.longestIncreasingSubsequence(test_data)
print(result)