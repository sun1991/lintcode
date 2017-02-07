# http://www.lintcode.com/en/problem/find-the-missing-number/

class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)

